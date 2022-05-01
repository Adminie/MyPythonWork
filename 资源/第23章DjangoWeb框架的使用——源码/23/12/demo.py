from django.urls import path
from app1 import views as app1_views
urlpatterns = [
    path('get_name', app1_views.get_name),
    path('get_name1', app1_views.PersonFormView.as_view()),
    path('person_detail/<int:pk>/', app1_views.person_detail),
]


