#user/models.py
from django.db import models


# Create your models here.
class ArticleModel(models.Model):
    class Meta:
        db_table = "Article"

    title = models.CharField(max_length=256)
    content = models.TextField()
    category = models.ForeignKey("CategoryModel", on_delete=models.CASCADE)


class CategoryModel(models.Model):
    class Meta:
        db_table = "Category"

    name = models.CharField(max_length=256,)
    explanation = models.TextField()