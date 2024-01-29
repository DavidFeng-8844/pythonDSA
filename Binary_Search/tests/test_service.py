import pytest
import Binary_Search.source.service as service
import unittest.mock as mock


@mock.patch("Binary_Search.source.service.database")
def test_get_user_from_db(get_user_from_db):
    with mock.patch("Binary_Search.source.service.database") as mock_db:
        mock_db.__getitem__.return_value = "david"
        result = service.get_user_from_db(1)
        assert result == "david"
        mock_db.__getitem__.assert_called_once_with(1)
