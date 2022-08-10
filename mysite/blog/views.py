from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView
from django.views.generic.dates import DayArchiveView, TodayArchiveView

from .models import Post

# -- ListView
class PostLV(ListView):
    model = Post
    template_name = 'blog/post_all.html' # template명을 지정하지 않으면 blog/post_list.html(default)로 저장되게 된다.
    context_object_name = 'posts' # template 파일로 넘겨주는 객체 리스트에 대한 context 변수명 설정
    paginate_by = 2 # 페이지 이동 버튼 (한 페이지에 보여주는 객체 리스트의 숫자 지정)

# -- DetailView
class PostDV(DetailView):
    model = Post  # default로 post_detail.html로 저장되게 된다.
    
# -- ArchiveView
class PostAV(ArchiveIndexView):
    # ArchiveIndexView는 테ㅣ블로부터 객체 리스트를 가져와 날짜 필드를 기준으로 가장 최신 객체를 먼저 출력
    model = Post
    date_field = 'modify_dt'

class PostYAV(YearArchiveView):
    model = Post
    date_field = 'modify_dt'
    make_object_list = True  # 해당 연도에 해당하는 객체의 리스트를 만들어서 template에 넘겨준다.

class PostMAV(MonthArchiveView):
    model = Post
    date_field = 'modify_dt'

class PostDAV(DayArchiveView):
    model = Post
    date_field = 'modify_dt'

class PostTAV(TodayArchiveView):
    model = Post
    date_field = 'modify_dt'
    
# tag용 클래스용 뷰 추가
class TagCloudTV(TemplateView):
    template_name = 'taggit/taggit_cloud.html'


class TaggedObjectLV(ListView):
    template_name = 'taggit/taggit_post_list.html'
    model = Post                                        # 대상 테이블은 Post 테이블

    def get_queryset(self):
        return Post.objects.filter(tags__name=self.kwargs.get('tag'))

    # tagging/taggit_post_list.html 에 넘겨줄 컨텍스트 변수를 추가하기 위해 get.. 메소드를 오버라이딩
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tagname'] = self.kwargs['tag']
        return context                                  # 템플릿 파일로 전달
