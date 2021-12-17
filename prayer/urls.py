from django.urls import path
from .views import prayer_views

app_name = 'prayer'

urlpatterns = [
    path('', prayer_views, name='prayer')
]

