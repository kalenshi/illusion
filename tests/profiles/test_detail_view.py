from django.http import Http404
from django.test import TestCase
from unittest.mock import Mock, patch

from core.profiles.detail_view import EmployeeProfileDetailView
from core.profiles.domain import ProfilesDomain


class TestDetailView(TestCase):
    """Test the profiles detail view"""

    def setUp(self) -> None:
        """Initialize required objects"""
        self.view = EmployeeProfileDetailView()
        self.domain = ProfilesDomain()

    @patch("core.profiles.domain.ProfilesDomain.get_profile")
    @patch("core.profiles.domain.Employee")
    def test_get(self, employee, domain):
        request = Mock()
        emp_no = 1
        employee.get.return_value = Mock()
        domain.return_value = domain

        response = self.view.get(request, emp_no)
        domain.assert_called_with(
            emp_no
        )
        self.assertEqual(response.status_code, 200)
