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


def __was_item_chosen_from_the_list(chosen_item):
    if chosen_item.startswith('list_item_'):
        return True
    else:
        return False


def __is_invalid(item_id):
    if item_id != 'Choose_item':
        return False
    else:
        return True


def __is_not_exponent_number(chosen_item):
    if 'e' not in chosen_item:
        return True
    else:
        return False


def __is_item_in_database(item_id):
    try:
        item_to_delete = Item.objects.get(id=item_id)
        return item_to_delete
    except ObjectDoesNotExist:
        return None


def delete_item_confirm(request):
    chosen_item = request.POST.get('id')
    
    #Check if item to delete was chosen from the list
    if __was_item_chosen_from_the_list(chosen_item):
        item_id = chosen_item.lstrip('list_item_')
        #Reject if option chosen from the list is not actual item
        if __is_invalid(item_id):
            messages.warning(
                request, f'Please choose an item from the list.')
            return redirect('delete-item')

    #If id was provided by the user, not chosen from the list:
    else:
        #Check id id was typed as an exponent number
        if __is_not_exponent_number(chosen_item):
            item_id = chosen_item
        else:
            #Reject if id was typed as an exponent number
            messages.warning(request, f'Exponent numbers are not allowed')
            return redirect('delete-item')
            
    #Look for an item in database and delete item if it exists
    item_to_delete = __is_item_in_database(item_id)
    if item_to_delete:
        context = {
            'item_to_delete': item_to_delete,
            'id': item_id
        }
        return render(request, 'storage/delete_item_confirm.html', context)
    else:
        messages.warning(request, f'Item with that ID could not be found.')
        return redirect('delete-item')


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
