import pytest
import requests
import unittest.mock as mock
import source.service as service


@mock.patch('source.service.get_user')
def test_service(mock_get):
    mock_get.return_value = 'Mocked Slowerzz'
    user_name = service.get_user(1)
    assert user_name == 'Mocked Slowerzz'


@mock.patch('requests.get')
def test_get_users(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {'id': 1, 'name': 'Bruno'}
    mock_get.return_value = mock_response
    data = service.get_user_from_db()
    assert data == {'id': 1, 'name': 'Bruno'}


@mock.patch('requests.get')
def test_get_users_error(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 400
    mock_get.return_value = mock_response
    with pytest.raises(requests.exceptions.HTTPError):
        service.get_user_from_db()
