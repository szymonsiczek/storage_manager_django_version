from django.shortcuts import render


def main_page(request):
    return render(request, 'storage/main.html')

def add_item(request):
    return render(request, 'storage/add_item.html')

def show_all(request):
    return render(request, 'storage/show_all.html')
    
def show_items_from_category(request):
    return render(request, 'storage/show_items_from_category.html')

def delete_item(request):
    return render(request, 'storage/delete_item.html')

def delete_all_items(request):
    return render(request, 'storage/delete_all_items.html')
