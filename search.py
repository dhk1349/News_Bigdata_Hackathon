#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 03:24:20 2019

@author: donghoon
"""
import requests  

def search(start, end,word):
    que=word[0]+" AND( "+word[1]+" OR "+word[2]+" OR "+word[3] + ")"
    url="http://tools.kinds.or.kr:8888/search/news"
    payload={
            "access_key":"c1e3b1cd-8d4c-4a6e-ba5c-d77a2c70e87b",
            "argument":
                {
                        "query":que,    
                        "published_at" : 
                            {
                                    "from":start+"T00:00:00.000Z",
                                    "until":end+"T00:00:00.000Z"
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
                        "return_size":5
                
            }
        }
    searcharticle=requests.post(url,json=payload)
    searcharticle=searcharticle.json()['return_object']['documents']
    contentresult=[]
    print("==============================================================================================")
    print("키워드 : ",word[1],",",word[2],", ",word[3],"\n")
    for i in searcharticle:
        del i['news_id']
        del i['published_at']
        del i['enveloped_at']
        del i['dateline']
        #del i['provider']
        x1="제목 "+i['title']
        x2="내용 \n"+i['hilight'].replace("<b>","").replace("</b>","").replace("<br>","\n")+"\n\n"
        print(x1+"\n"+x2)
        x1=x1+"\n"+x2+"\n\n"
        contentresult.append(x1)
    print("==============================================================================================")
    return contentresult

    
#search("2019-04-12",["버닝썬","성접대","YG"])
    
    

    
