import requests
import random
import time
headers={"Cookie": "XSRF-TOKEN=eyJpdiI6IjlnUXUyUUcwMTFRWFoxdlpPejVRSlE9PSIsInZhbHVlIjoiZU4wSy9XR2xQNUloSHN5dHNkeGthTjZybVdMTHlPd2xQdkxPQUNLYnhFNTJPbXFtM0RFUlowUGJDeFBGb3RnZDNuNmdzQ0NNeTBUWU1xdlZPUmJnMVk1RFZZbUtpYTBOdFZ4UFR6bnVRb0tTdDJWT2VpQTBHTllvQ0xrSExQUWsiLCJtYWMiOiJmYWZiNTgyNjg0ZDdlNTg5NTEwNGI5MDE3ZGU2NWFiYzdlNTFhYjk5NzA5ZjliZDFhZGY5NGMxNWQ5Nzk3Y2RmIiwidGFnIjoiIn0%3D; kyayzuutaw_session=eyJpdiI6Im1PT1dEZnVpUTUvSjI1NEc2UUxBS0E9PSIsInZhbHVlIjoiTWNEeVgvUHdKUU1aa1o2UStSeXNDVDE0TTA1VGUvbDUzNU1GY1A2Y1pVcHhQclRheE1NVDk3elhBcDY1TDQvLzc0Y1NHYWx2VEJoWkI0UEpYZzlNc0NGalNRZkI5KzFZY3RXLzE2amYzWTRINGpvc0JlQkNJZDFhWHg1ZEZJNUsiLCJtYWMiOiJiYWU4ZTg1MTIyZjJmMGQzNzE4YTJjMDYyNDE3ODVmNDg5NjM3ZDQ3ZDE1OGVhNjc4NjRjYmFiYTM1ZDM1NjI2IiwidGFnIjoiIn0%3D;",
"Content-Length": "93",
"Origin": "https://kyayzuutaw.com",
"Content-Type": "application/x-www-form-urlencoded",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
"Referer": "https://kyayzuutaw.com/blog/how-to-make-money-as-a-freelancer-check-out-our-tips",
"Accept-Encoding": "gzip, deflate",
"Accept-Language": "en-US,en;q=0.9"}


def url_loop(alias,token,headers):
    data=f"_token=TZiyx9oW6KvrLXNuf1wma5ooNlsRcB1VwLW2cHfJ&visitorId=xyf2z{token}&alias={alias}"
    res=requests.post("https://kyayzuutaw.com/blog/how-to-make-money-as-a-freelancer-check-out-our-tips",data=data,headers=headers,allow_redirects=False)
    return res.status_code
    

#url_loop("utvoi","gsaegw34",headers)

alias=[]
while True:
    code=input("Enter Your url Last digit::")
    if code == "":
        break
    else:
        alias.append(code)
print(alias)
timing=input("Enter loop times::")
delay=input("Enter Delay Time[ex,0.1,0.002:")
if delay == "":
    delay=0

for l_di in alias:
    print(l_di)
    for i in range(1,int(timing)+1):
        if url_loop(l_di,f"ags{random.randrange(111,999999)}bg{random.randrange(1,999)}y",headers) == 302:
            print(f"[{l_di}+{i}+--]OK>>",end="\r")
        else:
            print("URL LAST Code Not found")
        time.sleep(int(delay))
    print("DONE for "+l_di)





