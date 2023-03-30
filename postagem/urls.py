
from django.urls import path
from . import views
from .views import HomeView, DetalhesView, AddPostView, UpdatePostView, DeletePost, AddCategoryView, CategoryView, \
    CategoryListView, LikeView

urlpatterns = [
    #path("", views.inicio, name="home"),
    path('', HomeView.as_view(), name="home"),
    path('detalhes/<int:pk>', DetalhesView.as_view(), name="detalhes"),
    path('add_post/', AddPostView.as_view(), name="add_post"),
    path('add_category/', AddCategoryView.as_view(), name="add_category"),
    path('detalhes/edit/<int:pk>', UpdatePostView.as_view(), name='update'),
    path('detalhes/<int:pk>/remove', DeletePost.as_view(), name='delete_post'),
    path('category/<str:cats>/', CategoryView, name='category'),
    path('category-list/', CategoryListView, name='category-list'),
    path('like/<int:pk>', LikeView, name='like_post'),


]

