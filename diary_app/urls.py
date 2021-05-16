from django.urls import path
from . import views

urlpatterns = [
    path('', views.entry_display, name='entry_list'),
    path('new/', views.EntryCreate.as_view(), name='create_entry'),
    path('<int:pk>/edit/', views.Edit_entry.as_view(), name='edit_entry'),
    path('<int:pk>/delete/', views.Delete_entry.as_view(), name='delete_entry')
]
