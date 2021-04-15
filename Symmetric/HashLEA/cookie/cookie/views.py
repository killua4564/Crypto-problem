import os
import base64
from hashlib import sha256

from django.conf import settings
from django.http import HttpResponse
from django.template import RequestContext, Template
from django.views.decorators.http import require_http_methods



@require_http_methods(['GET'])
def admin(request):
    return HttpResponse(open(os.path.abspath(__file__), 'r').read())

@require_http_methods(['GET', 'POST'])
def index(request):
    assert len(settings.SECRET_KEY) == 50
    jwt = JWT(settings.SECRET_KEY.encode())

    if request.method == 'POST':
        response = HttpResponse('Hi guest')
        response.set_cookie('auth', jwt.sign({b'user': b'guest'}))
        return response
    if request.COOKIES.get('auth'):
        data = jwt.verify(request.COOKIES['auth'])
        if data and data.get(b'user'):    
            if data.get(b'user') == b'admin':
                if data.get(b'command'):
                    print(f'[Cookie] Command: {data.get(b"command").decode()}')
                    os.system(f'ls -al \'{data.get(b"command").decode().replace(" ", "")}\'')
                print('[FLAG] Cookie')
                return HttpResponse(f'Hi admin<br>Here\'s your flag: <code>{settings.FLAG}</code>')
            response = HttpResponse('Hi guest')
            response.set_cookie('auth', jwt.sign({b'user': b'guest'}))
            return response
        return HttpResponse(Template(
            '<form method=\'POST\'>{% csrf_token %}<input type=\'submit\' value=\'Guest\'></form>'
        ).render(RequestContext(request, {})))
    return HttpResponse(Template(
        '<form method=\'POST\'>{% csrf_token %}<input type=\'submit\' value=\'Guest\'></form>'
    ).render(RequestContext(request, {})))


class JWT:

    def __init__(self, key):
        self.key = key

    def sign(self, data):
        data = ('&'.join(f'{key.decode()}={value.decode()}' for key, value in data.items())).encode()
        sig = sha256(self.key + data).digest()
        data = base64.b64encode(data + sig)
        return data.decode()

    def verify(self, data):
        data = base64.b64decode(data.encode())
        data, sig = data[:-32], data[-32:]
        if sig == sha256(self.key + data).digest():
            return dict(item.split(b'=') for item in data.split(b'&') if item.count(b'=') == 1)
        return None
