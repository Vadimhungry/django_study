from django.shortcuts import render
import sys
from django.views import View

# имя текущего приложения
current_app_name = __package__ or (sys.argv[0] and sys.argv[0].split("/")[-2])

test_name = 'QWERTY_name'


class ArticleIndex(View):

    def get(self, request, *args, **kwargs):
        return render(
            request, 'article/index.html',
            context={'app_name': current_app_name, }
        )
