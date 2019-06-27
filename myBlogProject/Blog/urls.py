from django.urls import path
from . import views

# 프로젝트 urls.py에 다 표현하지 않은 라우팅들
urlpatterns = [
    path('', views.index, name="index"),
    path('new', views.new, name="new"),
    path('create', views.create, name="create"),
    path('<int:post_id>', views.detail, name="detail"),
    # 여기서 <int:post_id>는 www.com/updateForm/1 이라는 주소가 있을때,
    # 1을 정수로 post_id란 곳에 받겠다는 의미임.
    path('updateForm/<int:post_id>', views.updateForm, name="updateForm"),
    path('update/<int:post_id>', views.update, name="update"),
    path('delete/<int:post_id>', views.delete, name="delete"),
]