class NotFound(Exception):
    code = 404
    text = 'Page not Found'


class NotAllowed(Exception):
    code = 405
    text = 'Method not allowed'
