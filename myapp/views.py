# myapp/views.py

from django.shortcuts import render, redirect  # redirectに加えてrenderも必要
from .models import Post  # Postモデルを読み込む（これが抜けていました）

def index(request):
    posts = Post.objects.all()
    return render(request, 'myapp/index.html', {'posts': posts})

def create(request):
    if request.method == 'POST':
        Post.objects.create(
            title=request.POST['title'],
            content=request.POST['content']
        )
        return redirect('index')
    return render(request, 'myapp/create.html')

# myapp/views.py の最後に追加
from django.shortcuts import get_object_or_404

# 編集機能
def edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.save()
        return redirect('index')
    return render(request, 'myapp/edit.html', {'post': post})

# 削除機能
def delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('index')
    return render(request, 'myapp/delete_confirm.html', {'post': post})

# myapp/views.py の最後に追加

def chart(request):
    # 投稿の総数を数える
    post_count = Post.objects.count()
    # グラフに渡すデータを準備
    context = {
        'post_count': post_count,
    }
    return render(request, 'myapp/chart.html', context)