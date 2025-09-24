
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Order
from .forms import OrderForm


class OrderListView(ListView):
    model = Order
    template_name = 'basket/order_list.html'
    context_object_name = 'orders'

class OrderDetailView(DetailView):
    model = Order
    template_name = 'basket/order_detail.html'
    context_object_name = 'order'


class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'basket/order_form.html'
    success_url = reverse_lazy('order_list')


class OrderUpdateView(UpdateView):
    model = Order
    form_class = OrderForm
    template_name = 'basket/order_form.html'
    success_url = reverse_lazy('order_list')


class OrderDeleteView(DeleteView):
    model = Order
    template_name = 'basket/order_confirm_delete.html'
    success_url = reverse_lazy('order_list')
