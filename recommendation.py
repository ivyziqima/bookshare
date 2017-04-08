import user
import book

books = [] # list of book objects

def potential_recommend(c_user):
    p_recommend = []
    for book in books:
        if (book.author == c_user.author) or (book.subject == c_user.subject):
            p_recommend.append(book)
    return p_recommend

def recommend(c_user):
    p_recommend = potential_recommend(c_user)
    di = {}
    maxi = 0
    for book in p_recommend:
        matching = user.match(book.recommender)
        score = matching * book.rating
        if book.title not in di:
            di[book.title] = 0
        di[book.title] += score
    recommend = sorted(d.items(), key=lambda x: x[1])
    recommend = [book[0] for book in recommend]
    if len(recommend) >=20:
        return recommend[:20]
    else:
        return recommend


