def getHint(self, secret, guess):
    bulls = sum(map(operator.eq, secret, guess))
    both = sum(min(secret.count(x), guess.count(x)) for x in '0123456789')
    return '%dA%dB' % (bulls, both - bulls)
    
from collections import Counter
def getHint(self, secret, guess):
    bulls = sum(g == s for g, s in zip(secret, guess))
    cows = sum((Counter(secret) & Counter(guess)).values()) - bulls
    return "{0}A{1}B".format(bulls, cows)
