import requests
import random
import time
from bs4 import BeautifulSoup

def uag():
    aa='Mozilla/5.0 (Linux; Android'
    ver = random.choice(['1','2','3','4','5','6','7','8','9','10','11','12'])
    b=random.choice(['6','7','8','9','10','11','12','13'])
    c=f'Readmi Note;{ver}'
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    useragent=f'{aa} {b}; {c}) {g}{h}.{i}.{j}.{k} {l}'
    return useragent
def get_token(uag):
    res1=requests.get("https://kyayzuutaw.com/blog/types-of-artificial-intelligence-know-the-main-ones?token=q2e9u4sgrgsS544qw3039&alias=w2t7x",allow_redirects=False)

    cookies=(res1.cookies.get_dict())
    cookie=f"XSRF-TOKEN={cookies['XSRF-TOKEN']}; kyayzuutaw_session={cookies['kyayzuutaw_session']};alias={cookies['alias']};"
    
    
    headers1={"Cookie": cookie,
    "User-Agent": uag,
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.9"}
    res=requests.get("https://kyayzuutaw.com/blog/what-is-dao-know-the-importance-for-the-crypto-market",headers=headers1)
    coo=res.cookies.get_dict()
    cookie2=f"XSRF-TOKEN={coo['XSRF-TOKEN']}; kyayzuutaw_session={coo['kyayzuutaw_session']};"
    token=[]
    t_oken=[]
    soup = BeautifulSoup(res.text, 'html.parser')
    for txt in soup.find_all("input"):
        token.append(txt.attrs.get("value", ""))
    t_oken.append(token[0])
    t_oken.append(cookie2)
    return t_oken



def url_loop(alias,token,headers,token2):
    data=f"_token={token2[0]}&visitorId=xyf2z{token}&alias={alias}"
    res=requests.post("https://kyayzuutaw.com/blog/how-to-make-money-as-a-freelancer-check-out-our-tips",data=data,headers=headers,allow_redirects=False)
    
    return res.status_code
    

#url_loop("utvoi","gsaegw34",headers)

def code_gen():
    code=[]
    co=open("url.txt","r").read().splitlines()
    for i in co:
        code.append(i[21::])
    return code
timing=input("Enter loop times::")




alias=code_gen()

for i in range(1,int(timing)+1):
    l_di=alias[random.randrange(0,len(alias))]
    
    userag=uag()
    token=get_token(userag)

    headers2={"Cookie": token[1],
    "Content-Length": "93",
    "Origin": "https://kyayzuutaw.com",
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": userag,
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Referer": "https://kyayzuutaw.com/blog/how-to-make-money-as-a-freelancer-check-out-our-tips",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.9"}
    if url_loop(l_di,f"ags{random.randrange(111,999999)}bg{random.randrange(1,999)}y",headers2,token) == 302:
        print(f"[{l_di}+{i}+--]OK>>",end="\r")
    else:
        print("URL LAST Code Not found")
    time.sleep(random.randrange(1,50))

    





