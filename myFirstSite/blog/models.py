from django.conf import settings
from django.db import models
from django.utils import timezone
import urllib.request
import requests
from bs4 import BeautifulSoup


class Movie(models.Model):
    code = models.TextField()
    title = models.TextField()
    cast = models.TextField()
    characters = models.TextField()
    summary = models.TextField()
    famous_line = models.TextField()

    def __str__(self):
        return self.title

    def movieImg(self):
        realCode = int(self.code)
        url = "https://movie.naver.com/movie/bi/mi/photoViewPopup.nhn?movieCode=" + str(realCode)
        resp = requests.get(url)
        html = BeautifulSoup(resp.content, 'html.parser')
        imgUrl = html.find('img').attrs['src']
        return imgUrl

    def movieUrl(self):
        realCode = int(self.code)
        return "https://movie.naver.com/movie/bi/mi/basic.nhn?code=" + str(realCode)

ipython manage.py runserver
