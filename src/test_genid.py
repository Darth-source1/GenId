import unittest
from GenId import GenId


class TestGenId(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.gen = GenId("01")

    def test_gen_id(self):
        id = self.gen.get_id()
        self.assertGreaterEqual(int(id), 0)

    def test_next_id(self):
        id = self.gen.next_id()
        self.assertGreaterEqual(int(id), 0)
