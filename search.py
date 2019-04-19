#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 03:24:20 2019

@author: donghoon
"""
import requests

def search(date,word):
    que=word[0]+" AND( "+word[1]+" OR "+word[2]+" )"
    url="http://tools.kinds.or.kr:8888/search/news"
    payload={
            "access_key":"18694feb-ec22-408a-8f68-2947156608cb",
            "argument":
                {
                        "query":que,    
                        "published_at" : 
                            {
                                    "from":date+"T00:00:00.000Z",
                                    "until":date+"T24:00:00.000Z"
                            },
                        "provider":["",],
                        "category":["",],
                        "category_incident":[
                                "",
                                ],
                        "byline":"",
                        "provider_subject":[""],
                        "subject_info":[""],
                        "fields":[
                                "title"
                                "hilight"
                                ],
                        "sort":{"_score":"desc"},
                        "hilight":300,
                        "return_from":0,
                        "return_size":2
                
            }
        }
    searcharticle=requests.post(url,json=payload)
    searcharticle=searcharticle.json()['return_object']['documents']
    for i in searcharticle:
        del i['news_id']
        del i['published_at']
        del i['enveloped_at']
        del i['dateline']
        del i['provider']
        print("제목 "+i['title'])
        print("내용 \n"+i['hilight'].replace("<b>","").replace("</b>","").replace("<br>","\n")+"\n\n")
#search("2019-04-12",["버닝썬","성접대","YG"])
    
    

    
