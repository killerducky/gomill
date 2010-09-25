import unittest2

class SimpleTestCase(unittest2.TestCase):
    longMessage = True

    def __init__(self, fn):
        unittest2.TestCase.__init__(self)
        self.fn = fn
        try:
            self.name = fn.__module__.split(".", 1)[-1] + "." + fn.__name__
        except AttributeError:
            self.name = str(fn)

    def runTest(self):
        self.fn(self)

    def id(self):
        return self.name

    def shortDescription(self):
        return None

    def __str__(self):
        return self.name

    def __repr__(self):
        return "<repr SimpleTestCase: %s>" % self.name
