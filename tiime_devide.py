#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 16:45:00 2019

@author: donghoon
"""

import requests
from timeline import detect
from wordcloud import getwordcloud
#getwordcloud("버닝썬","2019-01-29")
#detect("버닝썬","2016-01-01")
def phasedevide(keyword,start):
    '''
    검색와 시작 날짜를 받아서 사건을 단계별로 구분해주는 함수
    매일마다 관련 키워드를 
    '''
    labels=detect("버닝썬","2016-01-01")
    final=[]
    for i in labels:
        #날짜 형식에 맞게 수정
        date=i['label'][0:4]+"-"+i['label'][4:6]+"-"+i['label'][6:8]
        #날짜별로 주요 관련어휘를 받아낼 것이다.
        result=getwordcloud("버닝썬",date)
        #날짜 단위로 날짜롸 관련 키워드를 저장할 변수이다.
        temp=[]
        temp.append(i['label'])
        count=0
        #우선 키워드를 10개만 담아보았다.
        for j in result:
            temp.append(j['name'])
            count+=1
            if(count==15):
                break;
        final.append(temp)
    for i in final:
        print(i)
    return final
phasedevide("a","a")