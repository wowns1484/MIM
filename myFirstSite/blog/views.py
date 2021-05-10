from django.shortcuts import render
from django.utils import timezone
from .models import Movie
import pymysql


def post_list(request):
    return render(request, 'blog/main.html')

def next_list(request):
    from konlpy.tag import Okt

    conn = pymysql.connect(host='localhost', user='root', password='1104', db='mim', charset='utf8')
    cursor = conn.cursor()

    sql = "SELECT * FROM blog_movie"
    cursor.execute(sql)
    movie = cursor.fetchall()
    print("complete load to movieData")

    code = []
    title = []
    data = []

    for eachMovie in movie:
        code.append(eachMovie[1])
        title.append(eachMovie[2])
        data.append(eachMovie[3] + eachMovie[4] + eachMovie[5] + eachMovie[6])

    print("complete save to movieData")

    okt = Okt()
    results = []
    text = request.GET["inputForm"]

    # 형태소 분석하기 . 단어의 기본형 사용
    malist = okt.pos(text, norm=True, stem=True)

    # 어미/조사/구두점 등은 대상에서 제외
    r = []

    for words in malist:
        if not words[1] in ["Josa", 'Eomi', 'Punctuation']:
            r.append(words[0])
    results.append(r)

    score = []

    for search in data:
        movieScore = 0
        # check = False
        for r in results[0]:
            if str(search).find(r) != -1:
                # index = str(search).find(r)
                # for i in range(len(r)):
                #     if r[i] != str(search)[index]:
                #         break
                #     index += 1
                #     if i == len(r) - 1:
                #         check = True
                # if check == True:
                movieScore += 1
        score.append(movieScore)

    print("complete assign score")

    idx = 0
    max = 2
    resultIdx = []
    for s in score:
        if s > max:
            max = s
            resultIdx.append(idx)
        idx += 1
    print("complete find movieIndex")

    for r in resultIdx:
        print(title[r])
        mvCode = code[r]

    movie = Movie.objects.filter(code=mvCode)

    return render(request, 'blog/next.html', {'movies': movie})