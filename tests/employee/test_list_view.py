from django.test import TestCase
from unittest.mock import Mock, patch

from core.employee.list_view import EmployeeListView
from core.employee.serializers import EmployeeSerializer


class TestListView(TestCase):
    """Test employee listView"""

    def setUp(self) -> None:
        self.view = EmployeeListView()
        self.serializer = EmployeeSerializer

    @patch("core.db_models.employee.Employee")
    def test_get(self, employee):
        """Test the get method"""
        request = Mock()
        employee.objects.all.return_value = Mock()
        response = self.view.get(request)

        self.assertEqual(response.status_code, 200)

    def test_post(self):
        """Test the post method"""
        request = Mock()
        request.data = {
            "birth_date": "1961-05-30",
            "first_name": "Kendra",
            "last_name": "Hofting",
            "gender": "M",
            "hire_date": "1986-03-14"
        }

        response = self.view.post(request)

        self.assertEqual(response.status_code, 201)
