from src.presentation.controllers.user_register_controller import UserRegisterController
from src.data.test.user_register import UserRegisterSpy
from src.presentation.http_types.http_response import HttpResponse


class HttpRequestMock:
    def __init__(self) -> None:
        self.body = {"first_name": "meuTeste", "last_name": "test_last", "age": 20}


def test_handler():
    http_request_mock = HttpRequestMock()
    use_case = UserRegisterSpy()
    user_find_controller = UserRegisterController(use_case)

    response = user_find_controller.handler(http_request_mock)

    assert isinstance(response, HttpResponse)
    assert response.status_code == 201
    assert response.body["data"] is not None
