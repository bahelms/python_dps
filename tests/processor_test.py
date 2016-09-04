import unittest
from dps import processor

class ProcessorTest(unittest.TestCase):
    @unittest.skip("Skip this")
    def test_source_data_is_persisted(self):
        processor.start()
        self.assertEqual("count query", "some integer")

    @unittest.skip("Skip this")
    def test_public_data_is_persisted(self):
        processor.start()
        self.assertEqual("count query", "some integer")

