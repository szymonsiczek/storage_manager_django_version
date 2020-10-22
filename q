[1mdiff --git a/storagemanager/storage/static/css/main.css b/storagemanager/storage/static/css/main.css[m
[1mindex a0bc57f..2402612 100644[m
[1m--- a/storagemanager/storage/static/css/main.css[m
[1m+++ b/storagemanager/storage/static/css/main.css[m
[36m@@ -28,6 +28,10 @@[m [mh3 {[m
   padding: 20px;[m
 }[m
 [m
[32m+[m[32ma #buttonlink {[m
[32m+[m[32m  text-decoration: none;[m
[32m+[m[32m}[m
[32m+[m
 .login_form {[m
   width: 400px;[m
   margin: auto;[m
[36m@@ -332,8 +336,8 @@[m [minput:focus {[m
   border-radius: 50%;[m
 }[m
 [m
[31m-.profile_photo {[m
[31m-  width: 200px;[m
[32m+[m[32m.div_profile_photo {[m
[32m+[m[32m  width: 700px;[m
   height: 200px;[m
   margin-top: 50px;[m
   margin-left: 50px;[m
[36m@@ -362,5 +366,21 @@[m [minput:focus {[m
   margin-left: 270px;[m
   top: -200px;[m
   font-style: italic;[m
[31m-  border: none;[m
[32m+[m[32m}[m
[32m+[m
[32m+[m[32m.update_profile_button {[m
[32m+[m[32m  position: relative;[m
[32m+[m[32m  width: 700px;[m
[32m+[m[32m  height: auto;[m
[32m+[m[32m  margin-left: 270px;[m
[32m+[m[32m  top: -188px;[m
[32m+[m[32m}[m
[32m+[m
[32m+[m[32m#cancel_updating_profile {[m
[32m+[m[32m  width: 150px;[m
[32m+[m[32m  text-align: center;[m
[32m+[m[32m  position: relative;[m
[32m+[m[32m  left: -250px;[m
[32m+[m[32m  left: -22px;[m
[32m+[m[32m  top: -90px;[m
 }[m
[1mdiff --git a/storagemanager/storage/views.py b/storagemanager/storage/views.py[m
[1mindex 658c9c3..2d6d366 100644[m
[1m--- a/storagemanager/storage/views.py[m
[1m+++ b/storagemanager/storage/views.py[m
[36m@@ -1,33 +1,37 @@[m
 from django.shortcuts import render, redirect[m
 from django.core.exceptions import ObjectDoesNotExist[m
 from django.contrib import messages[m
[31m-from django.views.generic import ListView, CreateView, DeleteView[m
 from django.contrib.auth.mixins import LoginRequiredMixin[m
[32m+[m[32mfrom django.contrib.auth.decorators import login_required[m
[32m+[m[32mfrom django.views.generic import ListView, CreateView, DeleteView[m
 from . models import Item[m
 [m
 [m
[32m+[m[32m@login_required[m
 def main_page(request):[m
     return render(request, 'storage/main.html')[m
 [m
 [m
[32m+[m[32m@login_required[m
 def add_item(request):[m
     return render(request, 'storage/add_item.html')[m
 [m
 [m
[31m-class AddItemCreateView(CreateView):[m
[32m+[m[32mclass AddItemCreateView(LoginRequiredMixin, CreateView):[m
     model = Item[m
     template_name = 'storage/add_item.html'[m
     fields = ['category', 'type', 'model', 'serial_number'][m
     success_url = '/'[m
 [m
 [m
[31m-class ShowAllListView(ListView):[m
[32m+[m[32mclass ShowAllListView(LoginRequiredMixin, ListView):[m
     model = Item[m
     template_name = 'storage/show_all.html'[m
     context_object_name = 'all_items'[m
     ordering = ['category', 'type', 'model'][m
 [m
 [m
[32m+[m[32m@login_required[m
 def show_items_from_category(request):[m
     chosen_category = request.POST.get('category')[m
     categories_set = sorted(Item.objects.values_list([m
[36m@@ -41,12 +45,14 @@[m [mdef show_items_from_category(request):[m
     return render(request, 'storage/show_items_from_category.html', context)[m
 [m
 [m
[32m+[m[32m@login_required[m
 def delete_item(request):[m
     context = {'all_items': Item.objects.all().order_by([m
         'category', 'type', 'model')}[m
     return render(request, 'storage/delete_item.html', context)[m
 [m
 [m
[32m+[m[32m@login_required[m
 def delete_item_confirm(request):[m
     if request.POST.get('id') == '':[m
         messages.warning(request, f'Please type a number')[m
[36m@@ -76,6 +82,7 @@[m [mdef delete_item_confirm(request):[m
         return render(request, 'storage/delete_item_confirm.html', context)[m
 [m
 [m
[32m+[m[32m@login_required[m
 def delete_item_after_confirm(request):[m
     item_to_delete = Item.objects.get(id=request.POST.get('id'))[m
     type = item_to_delete.type[m
[36m@@ -87,6 +94,7 @@[m [mdef delete_item_after_confirm(request):[m
     return redirect('delete-item')[m
 [m
 [m
[32m+[m[32m@login_required[m
 def delete_all_items(request):[m
     if request.method == 'POST':[m
         if request.POST.get('delete_all_confirmation') == 'yes':[m
[1mdiff --git a/storagemanager/storagemanager/settings.py b/storagemanager/storagemanager/settings.py[m
[1mindex bd44b7d..b975bfd 100644[m
[1m--- a/storagemanager/storagemanager/settings.py[m
[1m+++ b/storagemanager/storagemanager/settings.py[m
[36m@@ -125,3 +125,4 @@[m [mMEDIA_ROOT = BASE_DIR/'media'[m
 MEDIA_URL = '/media/'[m
 [m
 LOGIN_REDIRECT_URL = 'main-page'[m
[32m+[m[32mLOGIN_URL = 'login'[m
[1mdiff --git a/storagemanager/storagemanager/urls.py b/storagemanager/storagemanager/urls.py[m
[1mindex 351e713..f6ab4a7 100644[m
[1m--- a/storagemanager/storagemanager/urls.py[m
[1m+++ b/storagemanager/storagemanager/urls.py[m
[36m@@ -10,6 +10,7 @@[m [murlpatterns = [[m
     path('admin/', admin.site.urls),[m
     path('', include('storage.urls')),[m
     path('register/', user_views.register, name='register'),[m
[32m+[m[32m    path('profile/update', user_views.profile_update, name='profile-update'),[m
     path('profile/', user_views.profile, name='profile'),[m
     path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),[m
     path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout')[m
[1mdiff --git a/storagemanager/users/templates/users/profile.html b/storagemanager/users/templates/users/profile.html[m
[1mindex 1d7715d..7ce195a 100644[m
[1m--- a/storagemanager/users/templates/users/profile.html[m
[1m+++ b/storagemanager/users/templates/users/profile.html[m
[36m@@ -1,52 +1,19 @@[m
 {% extends "storage/base.html" %}[m
 {% block content %}[m
[31m-<div class="profile_photo">[m
[32m+[m[32m<div class="div_profile_photo">[m
         <img class="profile_pic" src="{{ user.profile.image.url }}" alt="Profile Picture">[m
 </div>[m
[31m-<!-- <div class="div_profile_username">[m
[32m+[m[32m<div class="div_profile_username">[m
     <span class="profile_username">{{ user.username }}</span>[m
[31m-</div> -->[m
[32m+[m[32m</div>[m
 <div class="div_profile_additional_info">[m
[31m-        <!-- <p>email: {{ user.email }}</p>[m
[31m-        <p>tel. {{ user.profile.phone_number }}</p>     -->[m
[31m-        <form method="POST" enctype="multipart/form-data">[m
[31m-                {% csrf_token %}[m
[31m-                <fieldset>[m
[31m-                        <legend>Update info</legend>[m
[31m-                        {{ u_form.non_field_errors }}[m
[31m-                        {{ p_form.non_field_errors }}[m
[31m-                        {% for field in u_form %}[m
[31m-                        <span class="form_error">{{ field.errors }}</span>[m
[31m-                        <span class="form_field_label">{{ field.label }}</span>[m
[31m-                        <div class="form_field_input">{{ field }}</div>[m
[31m-                        <div class="form_field_help_text">{{ field.help_text }}</div>[m
[31m-                        {% endfor %}[m
[31m-                        <!-- {{ p_form }} -->[m
[31m-                        {% for field in p_form %}[m
[31m-                        <span class="form_error">{{ field.errors }}</span>[m
[31m-                        {% if field.label == 'Image' %}[m
[31m-                                <span class="form_field_label">{{ field.label }}</span>[m
[31m-                                <div>{{ field }}</div>[m
[31m-                        {% else %}[m
[31m-                                <span class="form_field_label">{{ field.label }}</span>[m
[31m-                                <div class="form_field_input">{{ field }}</div>[m
[31m-                        {% endif %}[m
[31m-                        <div class="form_field_help_text">{{ field.help_text }}</div>[m
[31m-                        {% endfor %}[m
[31m-                </fieldset>[m
[31m-                <div class="centered"><button id="bluebutton" type="submit" >Update</button></div>[m
[31m-            </form>[m
[32m+[m[32m        <p>email: {{ user.email }}</p>[m
[32m+[m[32m        <p>tel. {{ user.profile.phone_number }}</p>[m[41m    [m
[32m+[m[32m</div>[m
[32m+[m[32m<div class="update_profile_button">[m
[32m+[m[32m        <form action="{% url 'profile-update' %}">[m
[32m+[m[32m        <button id="bluebutton">Update profile[m
[32m+[m[32m        </button>[m[41m [m
[32m+[m[32m        </form>[m
 </div>[m
[31m-<!-- <div class="registration_form">[m
[31m-        <!-- <form method="POST" enctype="multipart/form-data">[m
[31m-            {% csrf_token %}[m
[31m-            <fieldset>[m
[31m-                <legend>Profile Info</legend>[m
[31m-                {{ u_form }}[m
[31m-                {{ p_form }}[m
[31m-            </fieldset>[m
[31m-            <div class="centered"><button id="bluebutton" type="submit" >Update</button></div>[m
[31m-        </form> -->[m
[31m-    <!-- </div> --> [m
[31m-[m
 {% endblock content %}[m
\ No newline at end of file[m
[1mdiff --git a/storagemanager/users/templates/users/profileOLD.html b/storagemanager/users/templates/users/profileOLD.html[m
[1mdeleted file mode 100644[m
[1mindex 1dcfa8a..0000000[m
[1m--- a/storagemanager/users/templates/users/profileOLD.html[m
[1m+++ /dev/null[m
[36m@@ -1,13 +0,0 @@[m
[31m-{% extends "storage/base.html" %}[m
[31m-{% block content %}[m
[31m-<div class="profile_photo">[m
[31m-        <img class="profile_pic" src="{{ user.profile.image.url }}" alt="Profile Picture">[m
[31m-</div>[m
[31m-<div class="div_profile_username">[m
[31m-    <span class="profile_username">{{ user.username }}</span>[m
[31m-</div>[m
[31m-<div class="div_profile_additional_info">[m
[31m-        <p>email: {{ user.email }}</p>[m
[31m-        <p>tel. {{ user.profile.phone_number }}</p>    [m
[31m-</div>[m
[31m-{% endblock content %}[m
\ No newline at end of file[m
[1mdiff --git a/storagemanager/users/views.py b/storagemanager/users/views.py[m
[1mindex 467476e..238138d 100644[m
[1m--- a/storagemanager/users/views.py[m
[1m+++ b/storagemanager/users/views.py[m
[36m@@ -29,14 +29,14 @@[m [mdef register(request):[m
             phone_number = form.cleaned_data.get('phone_number')[m
             profile.add_phone_number(phone_number)[m
 [m
[31m-            return redirect('login')[m
[32m+[m[32m            return redirect('profile')[m
     else:[m
         form = UserRegisterForm()[m
     return render(request, 'users/register.html', {'form': form})[m
 [m
 [m
 @login_required[m
[31m-def profile(request):[m
[32m+[m[32mdef profile_update(request):[m
     if request.method == 'POST':[m
         u_form = UserUpdateForm(request.POST, instance=request.user)[m
         p_form = ProfileUpdateForm([m
[36m@@ -59,4 +59,9 @@[m [mdef profile(request):[m
         'p_form': p_form[m
     }[m
 [m
[31m-    return render(request, 'users/profile.html', forms)[m
[32m+[m[32m    return render(request, 'users/profile_update.html', forms)[m
[32m+[m
[32m+[m
[32m+[m[32m@login_required[m
[32m+[m[32mdef profile(request):[m
[32m+[m[32m    return render(request, 'users/profile.html')[m
