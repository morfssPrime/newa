from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='graduate'),
    path('wishes_universities',views.wishes_universities,name='wishes'),
    path('alumni_achievements',views.alumni_achievements,name='achievement'),
    path('create',views.create,name='create')
]