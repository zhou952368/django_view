import datetime
import decimal
import requests
import json
from collections import Iterable
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from demo04.models import Movie, Girl


def req(request):
    # request.GET
    # request.POST
    # request.method
    # request.COOKIES
    # request.session
    # request.FILES
    # request.path
    # request.META
    return HttpResponse()


# http://127.0.0.1/get/?page=1&size=10
# ?key = value&key = value
# request.GET  返回的类字典对象
def req_get(request):
    page = request.GET.get('page', 1)
    size = request.GET.get('size', 10)
    start = (page - 1) * size
    end = page * size
    # movies = Movie.objects.all()[start:end]
    # return HttpResponse(f"当前是第{page}页,第{size}行")
    # 已更新时间降序排列
    qs = Movie.objects.all().order_by('-update_time') if sorted else Movie.objects.all()
    movies = qs[start:end]
    for movie in movies:
        print(movie.name)
    return render()


"""
python 对象转化为json数据
1.获取数据  遍历数据库  获得数据
2.判断获得的数据是不是一个可迭代对象
3.将一条条python数据转化为json数据
"""


# 从数据库中获取数据 并将数据发送到to_list()判断数据是否是可迭代对象
def Movies(request):
    try:
        # 获取前十条数据
        movies = Movie.objects.all()
        # 将QuerySet对象的数据转化为列表套字典
        result = to_list(movies)
        data = {
            'status': 200,
            'msg': 'success',
            'data': result
        }
    except:
        # 发生抽取返回的数据
        data = {
            'status': 404,
            'msg': 'error'
        }
    return JsonResponse(data)


# 将从 Movies()中传递Python数据进行遍历判断
# 是否是可迭代对象 是就传递到obj_to_dict(obj)  进行Python数据逐条判断类型 转化为jsons数据
# 将QuerySet对象转化为列表套字典
def to_list(objects):
    li = []
    if objects and isinstance(objects, Iterable):
        for obj in objects:
            li.append(obj_to_dict(obj))
    return li


# 将对象转化为字典
def obj_to_dict(obj):
    result = {}
    if obj:
        # 将对象所有属性值转化为字典形式
        keys = vars(obj).keys()
        if keys:
            for key in keys:
                if not key.startswith('_'):
                    value = getattr(obj, key)
                    if isinstance(value, datetime.datetime):
                        value = value.strftime('%Y-%m-%d %H:%i:%s')
                    elif isinstance(value, datetime.date):
                        value = value.strftime('%Y-%m-%d')
                    elif isinstance(value, decimal.Decimal):
                        value = float(value)
                    result[key] = value
    return result


def load_date(request):
    response = requests.get('https://gank.io/api/data/%E7%A6%8F%E5%88%A9/600/1')
    welfare = json.loads(response.text)
    girls = []
    for obj in welfare['results']:
        girl = Girl()
        girl.type = obj.get('type')
        girl.source = obj.get('source')
        girl.desc = obj.get('desc')
        girl.created_date = obj.get('createdAt')
        girl.published = obj.get('publishedAt')
        girl.url = obj.get('url')
        girl.used = obj.get('used')
        girls.append(girl)
    Girl.objects.bulk_create(girls)
    return HttpResponse('so easy!!!!!')


def Tao(request):
    return render(request, 'TPP.html')
