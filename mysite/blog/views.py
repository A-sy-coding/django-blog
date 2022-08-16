from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView
from django.views.generic.dates import DayArchiveView, TodayArchiveView

from .models import Post
from django.conf import settings

# form 관련 뷰 라이브러리
from django.views.generic import FormView  
from blog.forms import PostSearchForm
from django.db.models import Q  # 검색 기능에 필요
from django.shortcuts import render

# 생성, 변경, 삭제를 위한 라이브러리
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from mysite.views import OwnerOnlyMixin

# -- ListView
class PostLV(ListView):
    model = Post
    template_name = 'blog/post_all.html' # template명을 지정하지 않으면 blog/post_list.html(default)로 저장되게 된다.
    context_object_name = 'posts' # template 파일로 넘겨주는 객체 리스트에 대한 context 변수명 설정
    paginate_by = 2 # 페이지 이동 버튼 (한 페이지에 보여주는 객체 리스트의 숫자 지정)

# -- DetailView
class PostDV(DetailView):
    model = Post  # default로 post_detail.html로 저장되게 된다.

    # javascript용 항목 추가
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['disqus_short'] = f"{settings.DISQUS_SHORTNAME}"
        context['disqus_id'] = f"post-{self.object.id}-{self.object.slug}"
        context['disqus_url'] = f"{settings.DISQUS_MY_DOMAIN}{self.object.get_absolute_url()}"
        context['disqus_title'] = f"{self.object.slug}"

        return context
    
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

#--- FormView   
class SearchFormView(FormView):
    form_class = PostSearchForm
    template_name = 'blog/post_search.html'

    def form_valid(self, form):
        searchWord = form.cleaned_data['search_word']
        post_list = Post.objects.filter(Q(title__icontains=searchWord) | Q(description__icontains=searchWord) | Q(content__icontains=searchWord)).distinct()

        context = {}
        context['form'] = form
        context['search_term'] = searchWord
        context['object_list'] = post_list

        return render(self.request, self.template_name, context) 

#--- Create, Update, DeleteView
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'slug', 'description', 'content']
    initial = {'slug': 'auto-filling-do-not-input'}
    success_url = reverse_lazy('blog:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class PostChangeLV(LoginRequiredMixin, ListView):
    template_name = 'blog/post_change_list.html'

    def get_queryset(self):
        return Post.objects.filter(owner=self.request.user)

class PostUpdateView(OwnerOnlyMixin, UpdateView):
    model = Post
    fields = ['title', 'slug', 'description', 'content']
    success_url = reverse_lazy('blog:index')

class PostDeleteView(OwnerOnlyMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('blog:index')