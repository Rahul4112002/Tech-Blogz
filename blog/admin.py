from django.contrib import admin
from .models import Category,Post

# For Configuration of Category Admin
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('image_tag','title','description','url','add_date')
    search_fields = ('title',)
    list_per_page = 50
    

# For Configuration of Post Admin
class PostAdmin(admin.ModelAdmin):
    list_display = ('image_tag','title','content','url','cat','add_date')
    search_fields = ('title',)
    list_filter = ('cat',)
    class Media:
        js = ('https://cdnjs.cloudflare.com/ajax/libs/tinymce/7.1.0/tinymce.min.js','js/script.js',)
    

# Register your models here.
admin.site.register(Category,CategoryAdmin)
admin.site.register(Post,PostAdmin)
