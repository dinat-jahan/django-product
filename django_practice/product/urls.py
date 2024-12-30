from django.urls import path
from .views import ProductView

from . import views



urlpatterns = [
    # path("",views.index,name="index"),
    path("",ProductView.as_view(),name="product-op"),
    path("<int:id>/",ProductView.as_view(),name="product-op-with-id"),

    # path("register/",RegisterView.as_view(),name='register'),
    # path("login/",LoginView.as_view(),name='login')
]