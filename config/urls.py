# config/urls.py
from django.contrib import admin
from django.urls import path, include  # include を忘れずに追加！

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),  # これで myapp/urls.py を読み込みます
]