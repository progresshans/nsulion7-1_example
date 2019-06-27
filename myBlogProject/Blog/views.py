from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post

# 글목록(글 전체를 보여줌)
def index(request):
    # Post라는 모델에서 전부 가져온 후 post_list에 담기
    post_list = Post.objects
    return render(request, 'index.html', {'post_list' : post_list})

# 글쓰기페이지 만들기
def new(request):
    return render(request, 'new.html')

# 실제 글쓰는 기능
def create(request):
    # Post 모델 클래스를 불러옴
    post = Post()
    # 각 필드별로 하나하나씩 실제값을 담기
    post.title = request.GET['title']
    post.content = request.GET['content']   
    post.user = request.user
    # 실제로 Post 모델에 저장하는 메소드
    post.save()

    return redirect('/post/')

# 자세하게 읽기(글 하나하나)
def detail(request, post_id):
    # Post모델에서 post_id값으로 찾아 한개만 가져오는데, 만약 존재하지 않는다면 404에러 띄우기
    post_detail = get_object_or_404(Post, pk=post_id)
    return render(request, 'detail.html', {'post' : post_detail})

# 글 수정하기 페이지 만들기
def updateForm(request, post_id):
    # Post모델에서 post_id값으로 찾아 한개만 가져오는데, 만약 존재하지 않는다면 404에러 띄우기
    post = get_object_or_404(Post, pk=post_id)
    #글 작성한 사람과 수정하기 요청한 사람이 다를 경우에는 못 가게 막음
    if(request.user != post.user):
        return redirect('/post')

    return render(request, 'updateForm.html', {'post' : post})

# 실제 글 수정하는 기능
def update(request, post_id):
    # Post모델에서 post_id값으로 찾아 한개만 가져오는데, 만약 존재하지 않는다면 404에러 띄우기
    post = get_object_or_404(Post, pk=post_id)
    post.title = request.GET['title']
    post.content = request.GET['content']
    post.save()
    return redirect('/post/')

# 글 삭제하기 기능
def delete(request, post_id):
    # Post모델에서 post_id값으로 찾아 한개만 가져오는데, 만약 존재하지 않는다면 404에러 띄우기
    post = get_object_or_404(Post, pk=post_id)
    # 글 작성한 사람과 수정하기 요청한 사람이 다를 경우에는 못 가게 막음
    if(request.user != post.user):
        return redirect('/post')
    # 글을 삭제하게 하는 메소드
    post.delete()
    return redirect('/post/')