from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


class IndexView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'index.html', context={
            'who': 'World',
        })



def about(request):
    return render(request, 'about.html')


def med_info_view(request, user_id, pet_id):
    context = {'user_id': user_id, 'pet_id': pet_id}
    print(context)
    return render(
        request,
        'med_info_template.html',
        context={'user_id': user_id, 'pet_id': pet_id}
    )
