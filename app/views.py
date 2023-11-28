from django.http import HttpResponse


def index(request):
    host = request.META["HTTP_HOST"]
    user_agent = request.META["HTTP_USER_AGENT"]
    path = request.path
        
    text = f'host: {host}, browser: {user_agent}, path: {path}'

    return HttpResponse(text, headers={'SecretCode': '1231247124'})


def user(request, name, age):
    return HttpResponse(f'User: {name}.  age: {age}')
