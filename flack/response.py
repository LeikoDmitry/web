
class Response:
    def __init__(self, status_code: int = 200, headers: dict = None, body: str = ''):
        self.status_code = status_code
        self.headers = {}
        self.body = b''
        self._set_base_headers()
        if headers is not None:
            self._update_headers(headers)
        self._set_body(body)

    def _set_base_headers(self):
        self.headers = {
            'Content-Type': 'text/html; charset=utf-8',
            'Content-Length': 0
        }

    def _set_body(self, raw_body: str):
        self.body = raw_body.encode('utf-8')
        self._update_headers(headers={
            'Content-Length': str(len(self.body))
        })

    def _update_headers(self, headers: dict):
        self.headers.update(headers)