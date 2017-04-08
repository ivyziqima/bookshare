import user

class book(object):
    '''
    A book object is constructed when a book is recommended.
    Attributes: title, author, subject, recommender
    '''
    def __init__(self, title, author, subject, recommender, rating):
        self.title = title
        self.author = author
        self.subject = subject
        book.review = None
        book.rating = rating
        book.recommender = recommender
    
    def add_review(self, user, review):
        self.review = review

    def add_rating(self, user, rating):
        self.rating = rating



     