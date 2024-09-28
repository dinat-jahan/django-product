
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("api/v1/product/",include("product.urls")),
    path('admin/', admin.site.urls),
]
