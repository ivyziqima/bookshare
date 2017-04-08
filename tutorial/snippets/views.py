from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from snippets.serializers import UserSerializer
from rest_framework import permissions
from snippets.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.decorators import detail_route

class BooksViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Books.objects.all()
    serializer_class = BooksSerializer

class UserprofileViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        userprofile = self.get_object()
        return Response(userprofile.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class BookList(generics.ListAPIView):
    """
    This uses that generic API list view to return a list
    of Question models as a response to GET requests. The queryset
    variable is the list of Question Models that ultimately gets
    serialized and returned to the User
    """

    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        search_term = self.request.query_params.get('search')

        # searching takes precendence over recommending
        if (search_term and self.request.method == 'GET'):
            queryset = Books.objects.filter(
                Q(title__icontains = search_term) |
                Q(subject__icontains = search_term) |
                Q(review__icontains = search_term)
            )

            return queryset

        # If we're not searching, send back some recommendations
        try:
            profile = UserProfile.objects.get(user=self.request.user)
        except UserProfile.DoesNotExist:
            profile = None

        if (profile):
            return recommendations.recommend(profile, Books)
        else:
            return Books.objects.all()
