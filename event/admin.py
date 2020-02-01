from django.contrib import admin
from .models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','start','end')
    list_filter = ('title',)
    fields = ['title','start','end']


admin.site.register(Post,PostAdmin)
admin.site.site_header = 'Calender admin panel'