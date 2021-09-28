import re
from abc import ABC
from typing import Type
from gunicorn.app.base import BaseApplication
from flack.exceptions import NotFound, NotAllowed
from flack.request import Request
from flack.response import Response
from flack.template_engine import Engine
from flack.view import View


class Flack(BaseApplication, ABC):
    def __init__(self, options=None):
        self.options = options or {}
        self.application = self.handler
        super().__init__()

    def load_config(self):
        config = {key: value for key, value in self.options.items()
                  if key in self.cfg.settings and value is not None}
        for key, value in config.items():
            self.cfg.set(key.lower(), value)

    @staticmethod
    def number_of_workers():
        return 2  # (multiprocessing.cpu_count() * 2) + 1

    def load(self):
        return self.application

    def handler(self, environ: dict, start_response):
        view = self._get_view(environ=environ)
        request = self._get_request(environ=environ)
        response = self._get_response(environ=environ, view=view, request=request)
        status = str(response.status_code)
        response_headers = response.headers
        start_response(status, response_headers.items())
        return iter([response.body])

    def _prepare_url(self, url: str):
        return url.strip('/')

    def _find_view(self, raw_url: str) -> Type[View]:
        url = self._prepare_url(raw_url)
        for path in self.options.get('urls', []):
            match_view = re.match(path.url, url)
            if match_view is not None:
                return path.view
        raise NotFound

    def _get_view(self, environ: dict) -> View:
        raw_url = environ.get('PATH_INFO', '')
        templates_path = self.options.get('base_dir', '') + '/' + self.options.get('templates_dir_name', '')
        return self._find_view(raw_url=raw_url)(Engine(template_paths=templates_path))

    def _get_request(self, environ: dict):
        return Request(environ=environ)

    def _get_response(self, environ: dict, view: View, request: Request) -> Response:
        request_method = environ.get('REQUEST_METHOD', 'GET').lower()
        if not hasattr(view, request_method):
            raise NotAllowed
        return getattr(view, request_method)(request)
