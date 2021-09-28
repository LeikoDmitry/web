from flack.urls import Url
from view import Index, Blog

urlpatterns = [
    Url('^$', Index),
    Url('^blog$', Blog)
]