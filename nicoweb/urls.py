from django.urls import path
#from . import views
from .views import HomeView, ArticleView, AddPostView, UpdatePostView, DeletePostView, AddCategoryView



urlpatterns = [
    #path('', views.home, name='home'),
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>/', ArticleView.as_view(), name='article'),
    path('add_post/', AddPostView.as_view(), name='addpost'),
    path('add_category/', AddCategoryView.as_view(), name='addcategory'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='editpost'),
    path('article/<int:pk>/remove', DeletePostView.as_view(), name='deletepost'),
]
