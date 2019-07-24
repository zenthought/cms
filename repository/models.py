from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
class Category(models.Model):
    name = models.CharField(verbose_name='类别名称', max_length=8)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(verbose_name='文章标题', max_length=32)
    category = models.ForeignKey('Category', blank=True, null=True, verbose_name='文章类别')
    summary = models.CharField(verbose_name='文章摘要', max_length=256)
    img = models.ImageField(upload_to='img/article/', verbose_name='显示图片', blank=True, default='img/article/123.jpg')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    detail = models.OneToOneField('ArticleDetail', verbose_name='文章详情')


class ArticleDetail(models.Model):
    content = RichTextUploadingField(verbose_name='文章详情')
