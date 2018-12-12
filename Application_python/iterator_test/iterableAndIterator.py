#coding=utf-8

from collections import Iterator,Iterable
import requests
class WeatherIterator:

    def __init__(self, cities):
        self.__cities = cities
        self.__index = 0

    def getWeather(self, city):
        r = requests.get('http://wthrcdn.etouch.cn/weather_mini?city='+city)
        data = r.json()['data']['forecast'][0]
        return '%s:%s,%s' % (city, data['low'], data['high'])

    def next(self):
        if self.__index == len(self.__cities):
            raise StopIteration
        weather = self.getWeather(self.__cities[self.__index])
        self.__index += 1
        return weather

class WeatherIterable:

    def __init__(self, cities):
        self.__cities = cities

    def __iter__(self):
        return WeatherIterator(self.__cities)



#TEST
cities = [u'北京',u'上海',u'广州',u'宁波']
for x in WeatherIterable(cities):
    print x