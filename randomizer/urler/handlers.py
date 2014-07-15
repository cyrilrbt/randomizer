import tornado
import random

import randomizer.handler
from randomizer.urler.models import Link


class URLerHandler(randomizer.handler.Handler):
    def get(self):
        # Show shit
        context = {
        }
        self.render("urler/new.html", **context)

    @tornado.gen.coroutine
    def post(self):
        # URLize shit
        n = random.choice(_worder.nouns)
        a = random.choice(_worder.adjs)
        while True:
            c = yield Link.objects.get(noun=n, adjective=a)
            if c is None:
                break
            n = random.choice(_worder.nouns)
            a = random.choice(_worder.adjs)

        print a, n
        l = yield Link.objects.create(
            url=self.get_argument('url'),
            noun=n,
            adjective=a,
        )
        context = {
            'awesome_url': l.link
        }
        self.render("urler/show.html", **context)


class RedirectHandler(randomizer.handler.Handler):
    @tornado.gen.coroutine
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

        words = []

        for l in open('/usr/share/wordnet/index.' + word_type):
            if l and not l.startswith(" "):
                w = l.split()[0].strip()
                if "_" not in w:
                    words.append(w)

        return words

_worder = Worder()
