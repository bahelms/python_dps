import unittest
from dps import Session, engine, processor
from dps.models.specatt import Specatt
from dps.models.spec_attribute import SpecAttribute
from tests import create_test_data, remove_test_data

class SpecattIntegrationTest(unittest.TestCase):
    def setUp(self):
        create_test_data("specatt")
        self.conn = engine.connect()
        self.trans = self.conn.begin()
        self.session = Session(bind=self.conn)

    def tearDown(self):
        remove_test_data()
        self.session.close()
        self.trans.rollback()
        self.conn.close()

    def test_source_data_is_persisted(self):
        processor.start(files="*_test.csv")
        count = self.session.query(Specatt).count()
        self.assertEqual(count, 5)

    def test_public_data_is_persisted(self):
        processor.start(files="*_test.csv")
        count = self.session.query(SpecAttribute).count()
        self.assertEqual(count, 5)

if __name__ == "__main__":
    unittest.main()
