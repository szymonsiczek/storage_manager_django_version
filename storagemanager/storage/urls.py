from django.urls import path
from . import views


urlpatterns = [
    path('', views.main_page, name='main-page'),
    path('add_item/', views.add_item, name='add-item'),
    path('show_all/', views.show_all, name='show-all'),
    path('show_items_from_category/', views.show_items_from_category, name='show-items-from-category'),
    path('delete_item/', views.delete_item, name='delete-item'),
    path('delete_all_items/', views.delete_all_items, name='delete-all-items'),
]