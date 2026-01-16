# myapp/admin.py
from django.contrib import admin
from .models import Post  # あなたが作ったPostモデルを読み込む

admin.site.register(Post)  # 管理画面に登録する