
# to create and populate the test venv:
# * python3 -m venv venv
# * source venv/bin/activate
# * pip install -r requirements.txt
# to execute these tests:
# * activate venv
#   source ./venv/bin/activate
# * execute tests
#   python -m unittest --verbose
# To execute only one test, suffix with the fully qualified test name. Example:
#   python -m unittest test.Test.test_NAME

from unittest import TestCase
from iris import Iris


class Test(TestCase):

    def setUp(self) -> None:
        self._subject = Iris()
        self._subject.start()

    def tearDown(self) -> None:
        self._subject.stop()

    def test_get_api_version_should_return_expected_version(self):
        api_version = self._subject.get_api_version()
        self.assertEqual('1.0.4', api_version)
