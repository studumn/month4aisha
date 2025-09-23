from django.shortcuts import render, get_object_or_404, redirect
from .models import Person, TourRegistration, HorseTour
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def tour_list(request):
    tours = TourRegistration.objects.all()
    return render(request, 'tour/tour_list.html', {'tours': tours})

def tour_detail(request, pk):
    tour = get_object_or_404(TourRegistration, pk=pk)
    return render(request, 'tour/tour_detail.html', {'tour': tour})

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


