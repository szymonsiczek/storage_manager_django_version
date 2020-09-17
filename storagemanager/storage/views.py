from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import ListView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from . models import Item
from operator import attrgetter


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
    context = {'all_items': sorted(Item.objects.all(), key=attrgetter('category', 'type', 'model'))}
    return render(request, 'storage/delete_item.html', context)

def delete_item_confirm(request):
    try:
        context = {'item_to_delete': str(Item.objects.filter(id=request.POST.get('id')).first()), 'id': request.POST.get('id')}
        return render(request, 'storage/delete_item_confirm.html', context)
    except ValueError:
        messages.warning(request, f'Please type a number')
        return redirect('delete-item')


def delete_item_after_confirm(request):
    item_var = Item.objects.filter(id=request.POST.get('id')).first()
    # item_to_delete = {'item_to_delete': item_var}
    Item.objects.filter(id=request.POST.get('id')).first().delete()
    messages.success(request, f'Item {item_var} has been deleted')
    return redirect('delete-item')
    # return render(request, 'storage/delete_item_after_confirm.html', item_to_delete)
    

class DeleteItemDeleteView(DeleteView):
    model = Item
#     template_name = 'deleteitem.html'
    pass

def delete_all_items(request):
    return render(request, 'storage/delete_all_items.html')

# 

