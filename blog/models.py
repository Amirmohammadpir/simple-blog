from django.db import models
from django.utils import timezone
from extentions.utils import jalali_converter

class Category(models.Model):
  title = models.CharField(max_length=200, verbose_name='عنوان')
  slug = models.SlugField(unique=True, verbose_name="آدرس")
  status = models.BooleanField(default=True, verbose_name="نمایش داده شود ؟")
  position = models.IntegerField(verbose_name='پوزیشن')

  class Meta:
    verbose_name = "دسته بندی"
    verbose_name_plural = "دسته بندی ها"
    ordering = ['position']

  def __str__(self):
    return self.title


class Article(models.Model):
  STATUS_CHOICE = [
    ("p" , "منتشر شده"),
    ('d' , 'پیش‌نویس'),
  ]

  title = models.CharField(max_length=200, verbose_name='عنوان')
  slug = models.SlugField(unique=True, verbose_name="آدرس")
  category = models.ManyToManyField(Category, verbose_name='دسته بندی', related_name = "articles")
  content = models.TextField(verbose_name="محتوا")
  published = models.DateTimeField(verbose_name="تاریخ انشتار")
  thumbnail = models.ImageField(upload_to='images/',default='default.jpg', verbose_name="عکس")
  created = models.DateTimeField(auto_now_add = True , verbose_name='تاریخ ایجاد')
  updated = models.DateTimeField(auto_now=True , verbose_name='آخرین ویرایش در')
  status = models.CharField(max_length=1, choices=STATUS_CHOICE, verbose_name='وضعیت انتشار')
  class Meta:
    verbose_name = 'مقاله'
    verbose_name_plural = 'مقالات'
    ordering = ['-published']
  
  def __str__(self):
    return self.title[:15]

  def jpublished(self):
    return jalali_converter(self.published)
  jpublished.short_description = 'زمان انتشار'