__author__ = 'Jack'


import listener, unittest


class TestListener(unittest.TestCase):

    def setUp(self):
        self.l = listener.Listener

    def test_exception(self):

        try:
            self.l.on_message(self, "", "Love")
            self.assertTrue(False)
        except NotImplementedError:
            self.assertTrue(True)