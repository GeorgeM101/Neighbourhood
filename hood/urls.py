from django.urls.conf import path
from . import views

urlpatters = [
    path('', views.index, name='index'),
    path('register',views.registration_form,name='registration_form'),

]
