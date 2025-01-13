from django.urls import path
from django.contrib.auth.views import LoginView
from .views import SignUpView, CustomLoginView

app_name = 'users'

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LoginView.as_view(), name='logout'),
]