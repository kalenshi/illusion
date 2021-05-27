from unittest.mock import patch, Mock

from django.test import TestCase


class TestProfilesDomain(TestCase):

    @patch("core.profiles.domain.Employee")
    def test_get_profile(self, employee_model):
        employee = Mock()
        employee_model.get.return_value = employee
        employee.get_salaries.return_value = [Mock(), Mock()]
        data = {
            "employee": {
                "emp_no": 1,
                "first_name": "first",
                "last_name": "last",
                "gender": "F",
                "hire_date": "1988-10-18"
            },
            "salaries": []

        }
