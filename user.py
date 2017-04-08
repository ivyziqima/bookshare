import util

class user(object):
    def __init__(self):
        self.interests = []
        self.subject = None
        self.author = None
        self.keyword = None

    def set_subject(self, subject):
        self.subject = subject

    def set_author(self, author):
        self.author = author

    def set_keyword(self, keyword):
        self.keyword = keyword

    def set_interest(self, interest):
        self.interests.append(interest)

    def match(self, other):
        v1 = util.interests_vector(self.interests)
        v2 = util.interests_vector(other.interests)
        n = len(v1)
        dist = util.probability_distribution(1/2, n)
        score = len([i for i in range(n) if v1[i] == v2[i]])
        match = 0
        for i in range(score + 1):
            match += dist[i]
        return match