from django.urls import path

from expense_tracker.web_app.views import index, edit

urlpatterns = [
    path('', index, name='index'),
    path('edit/<int:pk>/', edit, name='edit'),
]