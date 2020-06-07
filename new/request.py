# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 20:13:28 2020

@author: Neha Shinkre
"""
import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'Age':18, 'EstimatedSalary':9000})

print(r.json)

