from django.http import HttpResponse


def index(request):
    host = request.META["HTTP_HOST"]
    user_agent = request.META["HTTP_USER_AGENT"]
    ip = request.META["REMOTE_ADDR"]
    path = request.path

    text = f'host: {host}, browser: {user_agent}, path: {path}, ip: {ip}'

    return HttpResponse(text, headers={'SecretCode': '1231247124'})


def error(request, status=404, reason='Incorrect data'):
    return HttpResponse(f'Произошла ошибочка {status} {reason}')


def user(request, name='Undefied', age=0):
    return HttpResponse(f'User: {name},  age: {age}')
