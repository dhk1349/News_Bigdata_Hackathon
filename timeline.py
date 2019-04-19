#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 10:40:01 2019

@author: donghoon
"""
import datetime
import requests
def detect(keyword,start):
    '''
    키워드는 스트링 타입으로 입력
    start는 XXXX-XX-XX형식의 스트링타입으로 입력
    
    딕셔너리의 리스트 형식으로 리턴된다.
    딕셔너리내부에는'label','hits' 값을 가진다.
    '''
    now=datetime.datetime.now()
    today=now.strftime('%Y-%m-%d')
    url4="http://tools.kinds.or.kr:8888/time_line"
    payload4={
            "access_key": "18694feb-ec22-408a-8f68-2947156608cb",
            "argument": {
                    "query": keyword,
                    "published_at": {
                            "from": start,
                            "until": today
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
    timeline=requests.post(url4,json=payload4)
    timeline=timeline.json()['return_object']['time_line']
    newtimeline=[]
    for i in timeline:
        if(i['hits']>=20):
            newtimeline.append(i)
    #print(newtimeline)
    print("timeline finished")
    return newtimeline