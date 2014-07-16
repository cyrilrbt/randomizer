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
        url = self.get_argument('url')
        if not url.startswith('http://') or not url.startswith('https://'):
            url = 'http://%s' % url
        l = yield Link.objects.get(url=url)
        if not l:
            n = random.choice(_worder.nouns)
            a = random.choice(_worder.adjs)
            while True:
                c = yield Link.objects.get(noun=n, adjective=a)
                if c is None:
                    break
                n = random.choice(_worder.nouns)
                a = random.choice(_worder.adjs)

            l = yield Link.objects.create(
                url=url,
                noun=n,
                adjective=a,
            )
        self.redirect(self.reverse_url('urler_show', l._id))


class ShowHandler(randomizer.handler.Handler):
    @tornado.gen.coroutine
    def get(self, id):
        l = yield Link.objects.get(id=id)
        self.render("urler/show.html", link=l)


class RedirectHandler(randomizer.handler.Handler):
    @tornado.gen.coroutine
    def get(self, param):
        a, n = param.split('-')
        l = yield Link.objects.get(adjective=a, noun=n)
        self.redirect(l.url)


class Worder:
    def __init__(self):
        self.nouns = self.load_words('noun')
        self.adjs = self.load_words('adj')

    def load_words(self, word_type):
        """Returns a dict of first letter to set of words.
        """
        assert word_type in ["adj", "noun"]

        words = []

        #for l in open('/usr/share/wordnet/index.' + word_type):
        for l in open('/usr/local/Cellar/wordnet/3.1/dict/index.' + word_type):
            if l and not l.startswith(" "):
                w = l.split()[0].strip()
                if "_" not in w and "-" not in w:
                    words.append(w)

        return words

_worder = Worder()
