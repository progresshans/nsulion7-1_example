from django.db import models
from django.contrib.auth.models import User

# 글 데이터를 담아놓을 모델 클래스 생성, 이름은 Post라 함
class Post(models.Model):
    # 제목
    title = models.TextField()
    # 내용
    content = models.TextField()
    # 누가썼는가
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    # 언제썼는가
    pub_date = models.DateTimeField(auto_now=True)

