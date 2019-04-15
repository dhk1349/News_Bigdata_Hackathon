#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 10:40:00 2019

@author: donghoon
*서울의 감남 모 클럽처럼 버닝썬을 키워드가 들어가면 안나올 수도 있는 
것들을 포함시켜서 기사를 보여줄 수 있도록

*사건을 암시할 수 있는 사건 전의 작은 기사들을 캐치할 수 있는가? (의혹기)
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
            if(count==10):
                break;
        final.append(temp)
    for i in final:
        print(i)
    return final
phasedevide("a","a")
    
