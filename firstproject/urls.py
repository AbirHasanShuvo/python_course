from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
def h(request):
    return HttpResponse("This is Home Page for Abir")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', h)
]
