# -*- coding: utf-8 -*-
#encoding=utf-8

import urllib2
import sys
import json

id = raw_input() 

send_headers = {
    'Cookie' : 'appver=1.5.0.75771',
    'Content-Type' : 'application/x-www-form-urlencoded',
    'Referer' : 'http://www.xiami.com/'
    }
req = urllib2.Request('http://api.xiami.com/web?v=2.0&app_key=1&id='+id+'&r=song/detail',headers=send_headers)
response = urllib2.urlopen(req)
html = response.read()
receive_header = response.info()
musicdetail = json.loads(html)
print musicdetail['data']['song']['song_id']
print musicdetail['data']['song']['song_name']
print musicdetail['data']['song']['artist_name']
print musicdetail['data']['song']['listen_file']
print musicdetail['data']['song']['lyric']


