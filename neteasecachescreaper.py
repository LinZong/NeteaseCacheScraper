import os
import urllib2
import json


def SplitNeteaseMusicId(dir,file,wildcard,recursion):
    exts = wildcard.split(" ")
    for roots,subdirs,files,in os.walk(dir):
        for name in files:
            for ext in exts:
                if(name.endswith(ext)):
                    MusicId = name.split('-',-1)[0]
                    Olddir = os.path.join(dir,name)
                    JsonProcess(MusicId)
                    global Correctfilename
                    if not jsondetail['songs']:
                    
                        print "Cannot match the music,id is "+MusicId
                        
                    else:
                    
                        
                        Correctfilename = jsondetail['songs'][0]['name']
                        Newdir = os.path.join(dir,Correctfilename) +".mp3"
                        print "Found:"+Correctfilename
                        #os.rename(Olddir,Newdir)

                                     
                    
                    
                    break

def MainActivity():
    global dir
    dir = os.environ.get('USERPROFILE')+"\\AppData\\Local\\Netease\\CloudMusic\\Cache\\Cache"
    global dir1
    dir1 = os.environ.get('USERPROFILE')+"\\AppData\\Local\\Netease\\CloudMusic\\Cache\\Cache\\"
    global Tempdir
    wildcard = ".uc"
    SplitNeteaseMusicId(dir,file,wildcard,-1)
    os.system('explorer.exe '+dir1)

def JsonProcess(MusicId):
    response = urllib2.urlopen('http://music.163.com/api/song/detail/?id='+MusicId+'&ids=%5B'+MusicId+'%5D') 
    html = response.read()
    global jsondetail
    jsondetail = json.loads(html)
    
    

                               
MainActivity()
