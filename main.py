#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 10:40:00 2019

@author: donghoon
*서울의 감남 모 클럽처럼 버닝썬을 키워드가 들어가면 안나올 수도 있는 
것들을 포함시켜서 기사를 보여줄 수 있도록

*사건을 암시할 수 있는 사건 전의 작은 기사들을 캐치할 수 있는가? (의혹기)
"""
from timeline import detect
from wordcloud import getwordcloud
from time_divide import phasedivide ,keywordextract, GetNews

   

GetNews("버닝썬","2019-01-01")
