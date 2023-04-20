import requests
import random
import time
import string
from bs4 import BeautifulSoup
import json


def ext_cookie(data):
    c=[]
    res=(data["Set-Cookie"]).split(";")
    c.append(res[0])
    res2=(res[4]).split(",")
    c.append(res2[1][1::])
    return c

def uag():
    aa='Mozilla/5.0 (Linux; Android'
    ver = random.choice(['1','2','3','4','5','6','7','8','9','10','11','12'])
    b=random.choice(['6','7','8','9','10','11','12','13'])
    model=random.choice(["Redmi","Redmi","Huawei ","Huawei ","Oppo ","Oppo "])
    c=f'{model}{ver}'
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,225)
    i=random.randrange(73,225)
    j=random.randrange(120,225)
    k=random.randrange(40,225)
    l='Mobile Safari/537.36'
    useragent=f'{aa} {b}; {c}) {g}{h}.{i}.{j}.{k} {l}'
    return useragent
def get_token(uag,ali,idd):
    res1=requests.get(f"https://kyayzuutaw.com/blog/types-of-artificial-intelligence-know-the-main-ones?token={idd}&alias={ali}",allow_redirects=False)

    cookies=(res1.cookies.get_dict())
    
    cookie=f"XSRF-TOKEN={cookies['XSRF-TOKEN']}; kyayzuutaw_session={cookies['kyayzuutaw_session']};alias={cookies['alias']};"
    
    
    headers1={"Cookie": cookie,
    "User-Agent": uag,
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.9"}
    res=requests.get("https://kyayzuutaw.com/blog/how-to-make-the-family-budget-learn-5-tips",headers=headers1,allow_redirects=False)
    cok=res.headers
    
    coo=ext_cookie(cok)
    
    cookie2=f"{coo[0]}; {coo[1]};"
    token=[]
    t_oken=[]
    soup = BeautifulSoup(res.text, 'html.parser')
    for txt in soup.find_all("input"):
        
        token.append(txt.attrs.get("value", ""))
        
    
    t_oken.append(token[0])
    t_oken.append(cookie2)
    return t_oken



def url_loop(alias,token,headers,token2):
    data=f"_token={token2[0]}&visitorId={token}&alias={alias}"
    res=requests.post("https://kyayzuutaw.com/blog/how-to-make-money-as-a-freelancer-check-out-our-tips",data=data,headers=headers,allow_redirects=False)
    
    return res.status_code
    

#url_loop("utvoi","gsaegw34",headers)
def id_gen():
    letters=string.ascii_lowercase+string.digits
    
    rsult="".join(random.choices(letters,k=12))
    return rsult

def code_gen():
    code=[]
    co=open("url.txt","r").read().splitlines()
    for i in co:
        code.append(i[21::])
    return code
timing=input("Enter loop times::")



idd=id_gen()
alias=code_gen()

for i in range(1,int(timing)+1):
    l_di=alias[random.randrange(0,len(alias))]
    ll=l_di
    userag=uag()
    token=get_token(userag,ll,idd)
    sleep=random.randrange(1,50)

    headers2={"Cookie": token[1],
    "Content-Length": "93",
    "Origin": "https://kyayzuutaw.com",
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": userag,
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Referer": "https://kyayzuutaw.com/blog/how-to-make-money-as-a-freelancer-check-out-our-tips",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.9"}
    if url_loop(l_di,f"{idd}",headers2,token) == 302:
        print(f"[{l_di}+{i}+--]OK>>Sleep {sleep}",end="\r")
    else:
        print(f"URL LAST {ll} Not found {ll}")
    time.sleep(0)

    





