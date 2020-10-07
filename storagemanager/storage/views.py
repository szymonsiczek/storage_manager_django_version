from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
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
    ordering = ['category', 'type', 'model']


def show_items_from_category(request):
    chosen_category = request.POST.get('category')
    categories_set = sorted(Item.objects.values_list(
        'category', flat=True).distinct())
    sorted_items = Item.objects.filter(
        category=chosen_category).order_by('type', 'model')
    context = {
        'items_to_show': sorted_items,
        'categories': categories_set
    }
    return render(request, 'storage/show_items_from_category.html', context)


def delete_item(request):
    context = {'all_items': Item.objects.all().order_by(
        'category', 'type', 'model')}
    return render(request, 'storage/delete_item.html', context)


def delete_item_confirm(request):
    if request.POST.get('id') == '':
        messages.warning(request, f'Please type a number')
        return redirect('delete-item')
    elif 'e' in request.POST.get('id'):
        messages.warning(request, f'Exponent numbers are not allowed')
        return redirect('delete-item')
    else:
        item_id = request.POST.get('id')

    if item_id == 'Choose_item':
        messages.warning(request, f'Please choose an item from the list.')
        return redirect('delete-item')

    try:
        item_to_delete = Item.objects.get(id=item_id)
    except ObjectDoesNotExist:
        item_to_delete = None
    context = {
        'item_to_delete': item_to_delete,
        'id': item_id
    }
    if context.get('item_to_delete') == None:
        messages.warning(request, f'Item with that ID could not be found.')
        return redirect('delete-item')
    else:
        return render(request, 'storage/delete_item_confirm.html', context)


def delete_item_after_confirm(request):
    item_to_delete = Item.objects.get(id=request.POST.get('id'))
    type = item_to_delete.type
    model = item_to_delete.model
    serial_number = item_to_delete.serial_number
    item_to_delete.delete()
    messages.success(
        request, f'Item: {type} {model}, SN: {serial_number} has been deleted')
    return redirect('delete-item')


def delete_all_items(request):
    if request.method == 'POST':
        if request.POST.get('delete_all_confirmation') == 'yes':
            Item.objects.all().delete()
            messages.success(request, 'All items were deleted')
            return render(request, 'storage/delete_all_items.html')
    else:
        return render(request, 'storage/delete_all_items.html')
