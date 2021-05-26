from unittest.mock import patch, Mock

from django.test import TestCase


class TestProfilesDomain(TestCase):

    @patch("core.profiles.domain.Employee")
    def test_profile(self, employee_model):
        employee_model.get.return_value = Mock()

