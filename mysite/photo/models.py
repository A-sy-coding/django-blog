from django.db import models
from django.urls import reverse

from .fields import ThumbnailImageField

class Album(models.Model):
    '''
    Album은 같은 주제의 사진들을 모으는 역할
    '''
    name = models.CharField(max_length=30)
    description = models.CharField('One Line Description', max_length=100, blank=True)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name="OWNER", blank=True, null=True)

    class Meta:
        ordering = ('name',)  # name을 기준으로 오름차순
        
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('photo:album_detail', args=(self.id,))

class Photo(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    title = models.CharField('TITLE', max_length=30)
    description = models.TextField('Photo Description', blank=True)
    image = ThumbnailImageField(upload_to='photo/%Y/%m')
    upload_dt = models.DateTimeField('Upload Date', auto_now_add = True)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name="OWNER", blank=True, null=True)

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('photo:photo_detail', args=(self.id,))
