from django.contrib import admin
from student.models import Profile, Result

# Register your models here.

# if we want to see data in tabular format then need to use below class use list_display to see items like id,name etc.
# apart from this other things not required like in models file no need to return


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'roll', 'city')


admin.site.register(Profile, ProfileAdmin)


# also we can achieve using decorator
@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('id', 'stu_class', 'marks')
