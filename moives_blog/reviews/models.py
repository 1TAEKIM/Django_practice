from django.db import models
# movies 앱에 Movie model 가져오기
from movies.models import Movie 
from django.conf import settings

# Create your models here.
class reviews(models.Model):
    # 유저를 연결할 때에는 직접적으로 연결하지 않고, 간접 참조 권장(유지보수를 위해)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews')
    # 리뷰 작성 날짜
    review_date = models.DateField(auto_now_add=True)
    # 리뷰 영화 외래키
    review_movie = models.ForeignKey(Movie, to_field='title', on_delete=models.CASCADE)
    
    # 리뷰 제목
    review_title = models.TextField()
    # 리뷰 내용
    review_content = models.TextField()

class Comment(models.Model):
    
    content = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    review = models.ForeignKey(reviews, on_delete=models.CASCADE, related_name="comments")
    