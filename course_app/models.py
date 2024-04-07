from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

CHOOSE_TYPE = (
    ('Beckend', 'Beckend'),
    ('Frontend', 'Frontend'),
)


class CourseCategory(models.Model):
    category = models.CharField(max_length=25, choices=CHOOSE_TYPE)

    def __str__(self):
        return self.category


class CourseModel(models.Model):
    course_name = models.CharField(max_length=25, unique=True)
    course_category = models.ForeignKey(CourseCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.course_name


class ThemeModel(models.Model):
    id = models.IntegerField(default=None,primary_key=True, unique=True)
    course_name = models.ForeignKey(CourseModel, on_delete=models.CASCADE)
    theme_name = models.CharField(max_length=25, unique=True)
    theme_body = RichTextUploadingField()

    def __str__(self):
        return self.theme_name