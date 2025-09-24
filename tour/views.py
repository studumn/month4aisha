
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404, render
from .models import Person, TourRegistration, HorseTour


class TourListView(ListView):
    model = TourRegistration  
    template_name = 'tour/tour_list.html'
    context_object_name = 'tours'
    paginate_by = 5

class TourDetailView(DetailView):
    model = TourRegistration
    template_name = 'tour/tour_detail.html'
    context_object_name = 'tour'

def tour_register(request, person_id):
    person = get_object_or_404(Person, pk=person_id)
    registration, created = TourRegistration.objects.get_or_create(person=person)

    if created:
        message = "Регистрация прошла успешно!"
    else:
        message = "Вы уже зарегистрированы на тур!"

    return render(request, 'tour/tour_register.html', {
        'person': person,
        'registration': registration,
        'message': message
    })
