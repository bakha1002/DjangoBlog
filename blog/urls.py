from django.urls import path, include
from .views import *

urlpatterns = [
    path("list/", blog_list),
    path("list2/", BlogListView.as_view()),
]
