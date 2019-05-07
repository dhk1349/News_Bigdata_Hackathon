#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 16:45:00 2019

@author: donghoon
"""

from timeline import detect
from wordcloud import getwordcloud
from search import search
import operator
#getwordcloud("버닝썬","2019-01-29")
#detect("버닝썬","2016-01-01")
def keywordextract(keyword,start):
    '''
    검색와 시작 날짜를 받아서 사건을 단계별로 구분해주는 함수
    매일마다 관련 키워드를 
    '''
    labels=detect(keyword,start)#이슈의 보도 횟수 측정
    print("라벨에는 ",len(labels),"개가 있습니다.")
    final=[]
    #hits가 10회 이상인 날짜들을 가지고 있는 날짜 리스xm
    for i in labels:
        #날짜 형식에 맞게 수정
        date=i['label'][0:4]+"-"+i['label'][4:6]+"-"+i['label'][6:8]
        #날짜별로 주요 관련어휘를 받아낼 것이다.
        result=getwordcloud(keyword,date)        
        final.append(date)
        final.append(result)
        #print(final)

    print("keyword extract finished!")
    #["날짜1",[날짜1의 키워드와 가중치들...],]
    
    
    '''
    for i in final:
       print(i)
       ()
     '''
    #final은 날짜와 키워드 리스트들의 리스트이다.
    return final


def phasedivide(keyword,keywordlist):
    print("phasedivide function started\n")
    '''
    단계가 바뀌어야 하는 날짜를 lst에 기록하였다. 
    날짜는 인덱스 처리함
    lst가 리턴됨.
    
    input은 리스트 형태로 날짜, [키워드들,]의 반복이다.
    '''
    lst=[0]         #첫 번째 날짜 추가함
    count=7
    for i in range(3,len(keywordlist),2):   
        beforedaylist=[] #전 날의 키워드들은 모은다.
        for j in range(0,len(keywordlist[i-2])):
            beforedaylist.append(str(list(keywordlist[i-2][j].keys())[0]))
        
        if(str(list(keywordlist[i][0].keys())[0]) in beforedaylist or str(list(keywordlist[i][1].keys())[0]) in beforedaylist or str(list(keywordlist[i][2].keys())[0]) in beforedaylist):
            count-=1
            #만약 사건이 키워드의 큰 변화 없지 진행된다면 그냥 1주일에 한 번씩 업데이트 해준다.
            if(count==0):
                count=7
                lst.append(i-1)
                #단계가 나뉘었다는 표시를 해준다.
         #전날과 키워드가 다른 경우
        else:
            #단계가 나뉘었다고 표시해준다.
            lst.append(i-1)
            count=7
        #print(i,"th index passed!")
    return lst

def keyword_Integrate(timeline, keywordlist):
    print("keyword_Integrate fnc enter")
    '''
    기간을 나누고 그 기간동안 가장 중요한 키워드 추가
    
    return 값
    [기간, 키워드 딕셔너리]
    '''
    result=[]
    for i in range(1,len(timeline)):
        start=timeline[i-1]
        end=timeline[i]
        date=keywordlist[start]+"+"+keywordlist[end] #기간 표시
        result.append(date)
        
        weightbox={}
        for j in range(start+1,end,2):  #j에 지정한 기간동안의 일별 키워드+가중치들이 나옴
            temp=keywordlist[j]
            for k in range(0,len(temp)):  #각 일의 키워드를 하나씩 확인
                key=str(list(temp[k].keys())[0])
                value=float(list(temp[k].values())[0])
                if (weightbox.get(key)==None):
                    weightbox[key]=value
                    #print("new word",key,value)
                else:
                    weightbox[key]=weightbox.get(key)+value
                    #print("weight added",key,value,"->",weightbox[key])
        weightbox=sorted(weightbox.items(),key=operator.itemgetter(1),reverse=True)
        result.append(weightbox)
    #print(result)
    return result

def Newssearch(searchword,final_list):
    start=""
    end=""
    count=0
    result=[]
    for i in final_list:
        if(count%2==0): #날짜 
            print(i)
            start=i[:10]
            end=i[11:]
        else:
            words=[]
            words.append(searchword)
            words.append(i[0][0])
            words.append(i[1][0])
            words.append(i[2][0])
            article=search(start,end,words)
            print("======================================\n")
            print(article)
            print("======================================\n")
            result.append(words)
            result.append(article)
        count=count+1
    return result
def GetNews(keyword,start):
    keywordlist=keywordextract(keyword,start)    #모든 날짜와 날짜 별 키워드+가중치들이 있는 리스트
    timeline=phasedivide(keyword,keywordlist)    #기간을 나눌 인덱스
    final_list=keyword_Integrate(timeline,keywordlist)
    article=Newssearch(keyword, final_list)
    
    
    testfile=open("articel.txt",'w')
    for i in range(0,len(article)):
        testfile.write("==========================================\n")

        for j in article[i]:
            testfile.write(j)
            testfile.write("\n")
    testfile.close()
    return 0


    
   

    
    