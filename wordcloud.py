#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 11:12:10 2019

@author: donghoon
"""
import requests
def getwordcloud(keyword,date):
    '''
    키워드는 스트링타입으로 입력
    date는 특정 일자를 입력, 
    
    해당 일자에 키워드를 검색해서 나온 기사들의 관련어들을 
    가중치 순으로 정렬한다.

    딕셔너리 타입을 원소로 갖는 리스트를 리턴한다.
    딕셔너리는 id, name, level, weight를 값으로 가진다.
    
    weight가 가장 높은 키워드 10개가 가중치와 함께 리턴되며, 만약에 키워드가 10개 미만이면
    그 만큼만 리턴한다.
    '''
    url3="http://tools.kinds.or.kr:8888/word_cloud"
    payload3={
            "access_key": "c1e3b1cd-8d4c-4a6e-ba5c-d77a2c70e87b",
            "argument": {
                    "query": keyword,
                    "published_at": {
                            "from": date+"T00:00:00.000Z",
                            "until": date+"T24:00:00.000Z"
                            },
                            "provider": [
                                    "",
                                    ],
                            "category": [
                                    "",
                                    ],
                            "category_incident": [
                                    "",
                                    ],
                            "byline": "",
                            "provider_subject": [ "" ]
                            }
                }
    wordcloud=requests.post(url3,json=payload3)#워드 클라우드
    wordcloud=wordcloud.json()['return_object']['nodes']
    wordcloud=sorted(wordcloud,key=lambda wordcloud:(wordcloud['weight']),reverse=True)
    newlist=[]
    endpoint=10
    if(len(wordcloud)<endpoint):
        endpoint=len(wordcloud)
    for i in range(0,endpoint):
        temp={wordcloud[i]['name']:wordcloud[i]['weight']}
        newlist.append(temp)
    
    return newlist
    