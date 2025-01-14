from django.urls import path
#from .views import PhotoListView, PhotoDetailView, PhotoCreateView, PhotoUpdateView, PhotoDeleteView, PhotoTagListView
from . import views

app_name = 'photo'
urlpatterns = [
    path('', views.PhotoListView.as_view(), name='list'),
    path('photo/create/', views.PhotoCreateView.as_view(), name='create'),
    path('photo/<int:pk>/', views.PhotoDetailView.as_view(), name='detail'),
    path('photo/<int:pk>/update/', views.PhotoUpdateView.as_view(), name='update'),
    path('photo/<int:pk>/delete/', views.PhotoDeleteView.as_view(), name='delete'),
    path('tag/<slug:tag>/', views.PhotoTagListView.as_view(), name='tag'),
    # path('photo/<int:pk>/', views.CommentCreateView, name='detail'),
]