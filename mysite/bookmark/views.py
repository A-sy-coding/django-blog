from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Bookmark

class BookmarkLV(ListView):  # 모델명 소문자 => bookmark_list.html 형식의 이름으로 지정
    model = Bookmark

class BookmarkDV(DetailView): # 모델명 소문자 => bookmark_detail.html 형식의 이름으로 지정
    model = Bookmark
