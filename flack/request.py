from urllib.parse import parse_qs


class Request:
    GET = {}
    POST = {}

    def __init__(self, environ: dict):
        self.build_get_params_from_dict(environ.get('QUERY_STRING'))
        self.build_post_params_dict(environ.get('wsgi_input').read())

    def build_get_params_from_dict(self, raw_params: str):
        self.GET = parse_qs(raw_params)

    def build_post_params_dict(self, raw_bytes: bytes):
        self.POST = parse_qs(raw_bytes.decode('utf-8'))
