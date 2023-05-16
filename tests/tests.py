#  Copyright (C) 2023 Airbus CyberSecurity (SAS)
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU Lesser General Public
#  License as published by the Free Software Foundation; either
#  version 3 of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#  Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

# To create and populate the test venv:
#   python -m venv venv
#   source venv/bin/activate
#   pip install -r requirements.txt
# To activate venv and execute these tests:
#   source ./venv/bin/activate
#   python -m unittest --verbose
# To execute only one test, suffix with the fully qualified test name. Example:
#   python -m unittest tests.Tests.test_NAME

from unittest import TestCase
from iris import Iris


class Tests(TestCase):

    def setUp(self) -> None:
        self._subject = Iris()
        self._subject.start()

    def tearDown(self) -> None:
        self._subject.stop()

    def test_get_api_version_should_return_expected_version(self):
        api_version = self._subject.get_api_version()
        self.assertEqual('2.0.1', api_version)

    def test_create_case_should_add_a_new_case(self):
        case_count = self._subject.get_cases_count()
        customer_identifier = 1
        self._subject.create_case('case-name', 'Description', customer_identifier)
        self.assertEqual(case_count + 1, self._subject.get_cases_count())

    def test_export_case_should_not_fail(self):
        case_identifier = self._subject.create_case('case-name', 'Description', 1)
        case = self._subject.export_case(case_identifier)
        self.assertEqual('Description', case['case']['description'])

    def _get_module_by_human_name(self, module_human_name):
        modules = self._subject.list_modules()
        for module in modules:
            if module['module_human_name'] == module_human_name:
                return module
        raise LookupError(f'Module {module_human_name} not found')

    def test_register_module_should_not_fail(self):
        self._subject.register_module('iris_httpsend_module')
        module = self._get_module_by_human_name('Iris Http Send')
        self.assertIsNotNone(module)

    def test_register_module_should_enable_the_module(self):
        self._subject.register_module('iris_httpsend_module')
        module = self._get_module_by_human_name('Iris Http Send')
        self.assertTrue(module['is_active'])
