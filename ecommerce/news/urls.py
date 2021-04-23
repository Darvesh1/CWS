from django.urls import path
# from . import views
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', index, name="home"),
    path('news/category/<int:category_id>', get_category, name='category'),
]
