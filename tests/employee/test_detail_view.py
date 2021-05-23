from django.http import Http404
from django.test import TestCase
from unittest.mock import Mock, patch

from core.db_models.employee import Employee
from core.employee.detail_view import EmployeeDetailView
from core.employee.serializers import EmployeeSerializer


class TestDetailView(TestCase):
    """Test Employee DetailView"""

    def setUp(self) -> None:
        """Set up for the tests"""
        self.serializer = EmployeeSerializer
        self.view = EmployeeDetailView()

    @patch("core.db_models.employee.Employee")
    @patch("core.employee.detail_view.EmployeeDetailView")
    def test_get_object(self, detail_view, employee_model):
        """Test that creating an Employee works"""

        employee = Mock()
        employee_model.objects.get.return_value = Mock()
        detail_view.get_object.return_value = employee

        emp = detail_view.get_object(1)
        self.assertEqual(employee, emp)

    @patch("core.db_models.employee.Employee")
    def test_get_object_not_found(self, employee_model):
        """Tests get_object throws an exception"""
        employee_model.DoesNotExist = Employee.DoesNotExist
        employee_model.objects.get.side_effect = employee_model.DoesNotExist

        with self.assertRaises(Http404):
            self.view.get_object(1)

    @patch("core.employee.detail_view.Employee")
    def test_get(self, employee_model):
        """Test retrieving a single object"""

        request = Mock()
        employee = Mock()
        employee_model.objects.get.return_value = employee

        self.serializer.data = {
            "emp_no": 10090,
            "birth_date": "1961-05-30",
            "first_name": "Kendra",
            "last_name": "Hofting",
            "gender": "M",
            "hire_date": "1986-03-14"
        }
        response = self.view.get(request, emp_no=1)

        employee_model.objects.get.assert_called_with(
            pk=1
        )
        self.assertEqual(response.status_code, 200)
