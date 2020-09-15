from django.shortcuts import render
from . models import Item
from django.views.generic import ListView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


def main_page(request):
    return render(request, 'storage/main.html')

def add_item(request):
    return render(request, 'storage/add_item.html')

class AddItemCreateView(CreateView):
    model = Item
    template_name = 'storage/add_item.html'
    fields = ['category', 'type', 'model', 'serial_number']
    success_url = '/'

class ShowAllListView(ListView):
    model = Item
    template_name = 'storage/show_all.html'
    context_object_name = 'all_items'
    ordering = ['category', 'type']
    
def show_items_from_category(request):
    return render(request, 'storage/show_items_from_category.html')

def delete_item(request):
    pass

def delete_all_items(request):
    return render(request, 'storage/delete_all_items.html')
