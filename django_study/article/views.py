from django.shortcuts import render
import sys

# имя текущего приложения
current_app_name = __package__ or (sys.argv[0] and sys.argv[0].split("/")[-2])

test_name = 'QWERTY_name'

def index(request):
    return render(
        request, 'article/index.html',
        context={'app_name': current_app_name,}
    )
