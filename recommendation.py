from class_user import user
from class_book import book

creek = user()
a = book('hai di', 'fan er na', 'sci fi', creek, 10)
books = [a]

def potential_recommend(c_user):
    '''
    c_user: a user object
    '''
    if c_user.author == None and c_user.subject == None and c_user.keyword == None:
        return books
    else:
        p_recommend = []
        for book in books:
            if (book.author == c_user.author) or (book.subject == c_user.subject) or (c_user.keyword in book.review):
                p_recommend.append(book)
        return p_recommend

def recommend(c_user):
    p_recommend = potential_recommend(c_user)
    d = {}
    maxi = 0
    for book in p_recommend:
        matching = c_user.match(book.recommender)
        score = matching * book.rating
        if book.title not in d:
            d[book.title] = 0
        d[book.title] += score
    recommend = sorted(d.items(), key=lambda x: x[1])
    recommend = [book[0] for book in recommend]
    if len(recommend) >=20:
        return recommend[:20]
    else:
        return recommend


