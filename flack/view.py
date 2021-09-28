from abc import ABC, abstractmethod
from flack.request import Request
from flack.response import Response
from flack.template_engine import Engine


class View(ABC):

    def __init__(self, engine: Engine):
        self.engine = engine

    @abstractmethod
    def get(self, request: Request, *args, **kwargs) -> Response:
        pass

    def post(self, request: Request, *args, **kwargs) -> Response:
        pass
