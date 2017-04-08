import nltk
import user

class book(object):
    def __init__(self, title, author, subject, recommender):
        self.title = title
        self.author = author
        self.subject = subject
        book.recommender = recommender
    
    def add_review(self, user, review):
        self.review = review

    def add_rating(self, user, rating):
        self.rating = rating


     