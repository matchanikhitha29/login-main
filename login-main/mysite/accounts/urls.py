from django.urls import path
from .views import signup_view, login_view, project_home

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('project/', project_home, name='project_home'),
]
