from motorengine.document import Document
from motorengine import fields


class Link(Document):
    url = fields.StringField(required=True)
    adjective = fields.StringField(required=True)
    noun = fields.StringField(required=True)

    @property
    def link(self):
        return "http://urler.67labs.com/%s-%s" % (self.adjective, self.noun)
