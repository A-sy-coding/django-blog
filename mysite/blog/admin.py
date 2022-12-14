from django.contrib import admin
from .models import Post

# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title', 'modify_dt', 'tag_list')
#     list_filter = ('modify_dt',)
#     search_fields = ('title', 'content')
#     prepopulated_fields = {'slug': ('title',)}

#     # tag용 함수 2개 추가
#     def get_queryset(self, request):
#         return super().get_queryset(request).prefetch_related('tags')

#     def tag_list(self, obj):
#         return ', '.join(o.name for o in obj.tags.all())

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # list_display = ('id','title','modify_dt')
    list_display = ('id','title','modify_dt') 

    list_filter = ('modify_dt',)
    search_fields = ('title','content') # 검색 박스 표시, title, content 칼럼에서 검색
    prepopulated_fields = {'slug': ('title',)} # title 필드를 사용해 미리 채워지도록

