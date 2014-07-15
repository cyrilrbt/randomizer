import random
from collections import defaultdict

import randomizer.handler
from randomizer.urler.models import Link


class URLerHandler(randomizer.handler.Handler):
    def get(self):
        # Show shit
        context = {
        }
        self.render("urler/new.html", **context)

    def post(self):
        # URLize shit
        print self.get_argument('url')
        n, a = _worder.find_combo()
        l = Link(
            url=self.get_argument('url'),
            noun=n,
            adjective=a
        )
        l.save()
        context = {
            'awesome_url': l.link
        }
        self.render("urler/show.html", **context)


class RedirectHandler(randomizer.handler.Handler):
    def get(self, param):
        a, n = param.split('-')
        l = yield Link.objects.get(adjective=a, noun=n)
        self.redirect(l.link)


class Worder:
    def __init__(self):
        self.nouns = self.load_words('noun')
        self.adjs = self.load_words('adj')

    def load_words(self, word_type):
        """Returns a dict of first letter to set of words.
        """
        assert word_type in ["adj", "noun"]

        words = defaultdict(lambda: [])

        for l in open('/usr/local/Cellar/wordnet/3.1/dict/index.' + word_type):
            if l and not l.startswith(" "):
                w = l.split()[0].strip()
                if "_" not in w:
                    words[l[0].lower()].append(w)

        return words

    def find_combo(self):
        n = random.choice(self.nouns)
        a = random.choice(self.adjs)
        while Link.objects.filter(noun=n, adjective=a).count() > 0:
            n = random.choice(self.nouns)
            a = random.choice(self.adjs)
        return n, a


_worder = Worder()
