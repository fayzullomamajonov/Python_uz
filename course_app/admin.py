from django.contrib import admin
from .models import (
    CourseCategory,
    CourseModel,
    ThemeModel,
)


class ThemeModelAdmin(admin.ModelAdmin):
    list_display = ("id", "get_course_name", "theme_name")

    def get_course_name(self, obj):
        return obj.course_name.course_name

    get_course_name.short_description = "Course Name"


admin.site.register(CourseCategory)

admin.site.register(CourseModel)

admin.site.register(ThemeModel, ThemeModelAdmin)