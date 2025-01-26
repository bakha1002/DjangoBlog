from django.urls import path, include
from .views import *

urlpatterns = [
    path("my/", MyBlogView.as_view()),
    path("list/", blog_list),
    path("list2/", BlogListView.as_view()),
    path("<int:blogid>/", BlogDetailView.as_view()),
    path("create/", BlogCreateView.as_view()),
    path("update/<int:pk>/", BlogUpdateView.as_view()),
]
