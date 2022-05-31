#user/models.py
from django.db import models


# Create your models here.
class ArticleModel(models.Model):
    class Meta:
        db_table = "Article"

    title = models.CharField(max_length=20, null=False)
    category = models.CharField(max_length=256, null=False)
    content = models.ForeignKey("CategoryModel", max_length=256, null=False, on_delete=models.CASCADE)


class CategoryModel(models.Model):
    class Meta:
        db_table = "Category"

    name = models.CharField(max_length=20, null=False)
    explanation = models.CharField(max_length=256, default='')