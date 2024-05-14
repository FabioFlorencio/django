from django.contrib import admin
from django.urls import include, path

# usando url aninhada
urlpatterns = [
    path('', include('home.urls')),
    path('blog/',include('blog.urls')),
    path('admin/', admin.site.urls),
    
]
