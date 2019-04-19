#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 16:45:00 2019

@author: donghoon
"""

from timeline import detect
from wordcloud import getwordcloud
from search import search
#getwordcloud("버닝썬","2019-01-29")
#detect("버닝썬","2016-01-01")
def keywordextract(keyword,start):
    '''
    검색와 시작 날짜를 받아서 사건을 단계별로 구분해주는 함수
    매일마다 관련 키워드를 
    '''
    labels=detect(keyword,start)
    final=[]
    for i in labels:
        #날짜 형식에 맞게 수정
        date=i['label'][0:4]+"-"+i['label'][4:6]+"-"+i['label'][6:8]
        #날짜별로 주요 관련어휘를 받아낼 것이다.
        result=getwordcloud(keyword,date)
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
    #for i in final:
    #   print(i)
    #final은 날짜와 키워드 리스트들의 리스트이다.
    print("keyword extract finished!")
    return final


def phasedivide(keyword,keywordlist):
    temp=[keywordlist[0][0],keywordlist[0][1],keywordlist[0][2]]
    lst=[temp]
    for i in range(1,len(keywordlist)):
        if(keywordlist[i][1] in keywordlist[i-1] or keywordlist[i][2] in keywordlist[i-1] or keywordlist[i][3] in keywordlist[i-1]):
            #키워드가 전 일과 유사한 경우
            continue
        #아닌 경우
        temp=[keywordlist[i][0],keywordlist[i][1],keywordlist[i][2]]
        lst.append(temp)
    for i in lst:
        i[0]=i[0][0:4]+"-"+i[0][4:6]+"-"+i[0][6:8]
        print("\n\n\n=======================================================")
        print(i[0]+" 일자 뉴스")
        print("키워드:  "+i[1]+" "+i[2])
        search(i[0],[keyword,i[1],i[2]])
        
    
    
    
    
    
    