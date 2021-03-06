from unittest import TestCase, mock
from ..admin import DosUserInline
from ..models import CapacityAuthDosUser


class TestDosUserInline(TestCase):
    @mock.patch("api.authentication.admin")
    @mock.patch("api.authentication.admin.super")
    def test_get_exclude__new_list(self, mock_super, mock_admin):
        admin = DosUserInline(CapacityAuthDosUser, mock_admin)
        dummy_request = "dummy-request"
        dummy_object = "dummy-object"
        mock_super().get_exclude.return_value = None

        exclude = admin.get_exclude(dummy_request, dummy_object)

        mock_super().get_exclude.assert_called_with(dummy_request, dummy_object)
        self.assertListEqual(["dos_user_id"], exclude)

    @mock.patch("api.authentication.admin")
    @mock.patch("api.authentication.admin.super")
    def test_get_exclude__append_list(self, mock_super, mock_admin):
        admin = DosUserInline(CapacityAuthDosUser, mock_admin)
        dummy_request = "dummy-request"
        dummy_object = "dummy-object"
        mock_super().get_exclude.return_value = [
            "fake_exclude_field",
        ]

        exclude = admin.get_exclude(dummy_request, dummy_object)

        mock_super().get_exclude.assert_called_with(dummy_request, dummy_object)
        self.assertListEqual(["fake_exclude_field", "dos_user_id"], exclude)
