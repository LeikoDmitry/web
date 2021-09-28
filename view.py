from flack.request import Request
from flack.response import Response
from flack.view import View


class Index(View):
    def get(self, request: Request, *args, **kwargs):
        body = self.engine.render('home.html', context={
            'name': 'home'
        })
        return Response(body=body, headers={'Content-Type': 'text/html; charset=utf-8'})


class Blog(View):
    def get(self, request: Request, *args, **kwargs):
        post_id = request.GET.get('id', '')
        if not post_id:
            return Response(body='This is blog')
        return Response(body=post_id[0])
