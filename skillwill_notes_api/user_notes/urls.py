from django.urls import path
from . import views

urlpatterns = [
    path('', views.NoteCollectionView.as_view())
]