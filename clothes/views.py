from django.views.generic import ListView
from .models import Clothes, Tag

class ClothesListView(ListView):
    model = Clothes
    template_name = 'clothes/clothes_list.html'
    context_object_name = 'clothes'
    paginate_by = 5  

    def get_queryset(self):
        tag = self.request.GET.get('tag')  
        if tag:
            return Clothes.objects.filter(tags__name=tag)
        return Clothes.objects.all()
