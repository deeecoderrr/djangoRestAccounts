from django.urls import include, re_path
from . import views

urlpatterns = [
    re_path(r'create/$', views.UserCreate.as_view(), name='account-create'),
    re_path('hello/', views.HelloView.as_view(), name='hello'),
]


