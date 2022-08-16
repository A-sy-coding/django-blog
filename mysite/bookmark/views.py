from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Bookmark

# 생성, 수정, 변경, 삭제를 위한 라이브러리
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from mysite.views import OwnerOnlyMixin

class BookmarkLV(ListView):  # 모델명 소문자 => bookmark_list.html 형식의 이름으로 지정
    model = Bookmark

class BookmarkDV(DetailView): # 모델명 소문자 => bookmark_detail.html 형식의 이름으로 지정
    model = Bookmark

class BookmarkCreateView(LoginRequiredMixin, CreateView):
    '''
    북마크 생성 클래스
    '''
    model = Bookmark
    fields = ['title', 'url']
    success_url = reverse_lazy('bookmark:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class BookmarkChangeLV(LoginRequiredMixin, ListView):
    '''
    북마크 변경가능 리스트 보여주는 클래스
    '''
    template_name = 'bookmark/bookmark_change_list.html'

    def get_queryset(self):
        return Bookmark.objects.filter(owner=self.request.user)

class BookmarkUpdateView(OwnerOnlyMixin, UpdateView):
    '''
    북마크 업데이트 클래스
    '''
    model = Bookmark
    fields = ['title', 'url']
    success_url = reverse_lazy('bookmark:index')

class BookmarkDeleteView(OwnerOnlyMixin, DeleteView):
    '''
    북마크 삭제 클래스
    '''
    model = Bookmark
    success_url = reverse_lazy('bookmark:index')