import unittest
from dps import Session, processor
from dps.models.specatt import Specatt
from dps.models.spec_attribute import SpecAttribute
from tests import db_support, create_test_data, remove_test_data

Session.configure(bind=db_support.engine)

class SpecattIntegrationTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        create_test_data("specatt")

    @classmethod
    def tearDownClass(cls):
        remove_test_data()

    def setUp(self):
        self.session = Session()

    def tearDown(self):
        self.session.query(Specatt).delete()
        self.session.query(SpecAttribute).delete()
        self.session.commit()
        self.session.close()

    def test_source_data_is_persisted(self):
        processor.start(directory="test_data")
        count = self.session.query(Specatt).count()
        self.assertEqual(count, 5)

    def test_public_data_is_persisted(self):
        processor.start(directory="test_data")
        count = self.session.query(SpecAttribute).count()
        self.assertEqual(count, 5)

if __name__ == "__main__":
    unittest.main()
