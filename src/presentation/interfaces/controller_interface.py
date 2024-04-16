from abc import ABC, abstractmethod
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse


class ControllerInterface(ABC):

    @abstractmethod
    def handler(self, http_request: HttpRequest) -> HttpResponse:
        pass
