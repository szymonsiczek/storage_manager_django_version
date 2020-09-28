from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import ListView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from . models import Item



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
    categories_set = set()                      
    for item in Item.objects.all():
        categories_set.add(item.category)
    sorted_items = Item.objects.filter(category=request.POST.get('category')).order_by('type', 'model')
    context = {
        'items_to_show': sorted_items, 
        'categories': categories_set
        }
    return render(request, 'storage/show_items_from_category.html', context)

def delete_item(request):
    context = {'all_items': Item.objects.all().order_by('category', 'type', 'model')}
    return render(request, 'storage/delete_item.html', context)

def delete_item_confirm(request):
    if request.POST.get('id') == 'Choose_item':
        messages.warning(request, f'Please choose an item from the list.')
        return redirect('delete-item')
    try:
        context = {
            'item_to_delete': str(Item.objects.filter(id=request.POST.get('id')).first()), 
            'id': request.POST.get('id')
            }
        if context.get('item_to_delete').startswith('None'):
            messages.warning(request, f'Item with that ID could not be found.')
            return redirect('delete-item')
        else:
            return render(request, 'storage/delete_item_confirm.html', context)
    except ValueError:
        messages.warning(request, f'Please type a number')
        return redirect('delete-item')

def delete_item_after_confirm(request):
    item_var = Item.objects.filter(id=request.POST.get('id')).first()
    Item.objects.filter(id=request.POST.get('id')).first().delete()
    messages.success(request, f'Item: {item_var.type} {item_var.model}, SN: {item_var.serial_number} has been deleted')
    return redirect('delete-item')

def delete_all_items(request):
    if request.method == 'POST':
        if request.POST.get('delete_all_confirmation') == 'yes':
            for item in Item.objects.all():
                item.delete()
            messages.success(request, 'All items were deleted')
            return render(request, 'storage/delete_all_items.html')
    else:       
        return render(request, 'storage/delete_all_items.html')


