from src.presentation.controllers.user_finder_controller import UserFinderController
from src.data.test.user_finder import UserFinderSpy
from src.presentation.http_types.http_response import HttpResponse


class HttpRequestMock:
    def __init__(self) -> None:
        self.query_params = {"first_name": "meuTeste"}


def test_handler():
    http_request_mock = HttpRequestMock()
    use_case = UserFinderSpy()
    user_find_controller = UserFinderController(use_case)

    response = user_find_controller.handler(http_request_mock)

    assert isinstance(response, HttpResponse)
    assert response.status_code == 200
    assert response.body["data"] is not None
