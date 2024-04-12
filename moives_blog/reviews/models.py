from django.db import models
# movies 앱에 Movie model 가져오기
from movies.models import Movie 

# Create your models here.
class reviews(models.Model):
    # 리뷰 작성 날짜
    review_date = models.DateField(auto_now_add=True)
    # 리뷰 영화 외래키
    review_movie = models.ForeignKey(Movie, to_field='title', on_delete=models.CASCADE)
    
    # 리뷰 제목
    review_title = models.TextField()
    # 리뷰 내용
    review_content = models.TextField()
