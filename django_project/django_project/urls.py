from django.contrib import admin
from django.urls import path
from My_Application import views   # correct

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # example
    # other paths...
]
