from django.contrib import admin
from .models import ArticleModel
from .models import CategoryModel

# Register your models here.
admin.site.register(ArticleModel) # 이 코드가 나의 UserModel을 Admin에 추가 해 줍니다
admin.site.register(CategoryModel)