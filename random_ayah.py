#!/usr/bin/env python3

# -------------------------------------------------
# RANDOM AYAH + TAFSEER
# -------------------------------------------------
# THIS SCRIPT CALLS USES (alquran.cloud) API TO GET A RANDOM VERSE FROM THE HOLY QURAN AND IT'S TAFSEER (EXPLANATION) AND PRINTS THEM TO THE CONSOLE
# هذا السكربت يقوم بايجاد اية عشوائية من القران الكريم بالاضافة الى تفسيرها ويقوم بطباعتها في النتيجة
# -------------------------------------------------

import requests
import json
import random
import time

num = random.randint(1,6000)
url = "http://api.alquran.cloud/v1/ayah/"+str(num)
res = requests.get(url)
data = res.json()
surah =  data['data']['surah']['number']
ayah = data['data']['numberInSurah']

tafseer_url=url = "http://api.alquran.cloud/v1/ayah/"+str(num)+"/ar.muyassar"
tafseer = requests.get(tafseer_url).json()['data']['text']

print('Session Aya')
print('---')
print(data['data']['text'])
print('---')
print('التفسير:')

# This part makes a new line every 20 words so the text doesn't become long
# هذا الجزء يقوم بانشاء سطر جديد كل 20 كلمة حتى ﻻ يصبح النص طويل
tafseer_arr = tafseer.split()
n = 0
tafseer_text=""
for i in tafseer_arr:
    i = i + " "
    tafseer_text += i

    n+=1

    if n == 20:
        tafseer_text += "\n"
        n = 0

print(tafseer_text)
