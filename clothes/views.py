from django.shortcuts import render
from .models import Clothes , Tag

def clothes_list(request):
    tag_name = request.GET.get('tag')
    if tag_name:
        all_clothes = Clothes.objects.filter(tags__name=tag_name)
    else:
        all_clothes = Clothes.objects.all()
    return render(request, 'clothes/clothes_list.html', {'clothes': all_clothes})
