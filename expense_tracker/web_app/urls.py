from django.urls import path

from expense_tracker.web_app.views import index

urlpatterns = [
    path('', index, name='index')
]