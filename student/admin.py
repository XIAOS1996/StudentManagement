from django.contrib import admin

# Register your models here.
from .models import SchoolModel, StudentModel, StudentDetailsModel, GradeClassModel


# @admin.register(SchoolModel)
class SchoolAdmin(admin.ModelAdmin):
    pass


@admin.register(GradeClassModel)
class GradeClassAdmin(admin.ModelAdmin):
    list_display = ('s_grade', 's_class', 'cnt', 'create_time',)
    list_filter = ('s_grade',)
    ordering = ('s_grade', 's_class')


@admin.register(StudentModel)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('uuid','name', 'in_class', 'create_time')
    list_display_links = ('uuid',)

    ordering = ('in_class', 'uuid')


class StudentDetailsAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'gender', 'telephone', 'card_num', 'address',)
    list_display_links = ('uuid',)


admin.site.register(StudentDetailsModel, StudentDetailsAdmin)
