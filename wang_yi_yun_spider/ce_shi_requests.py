#Author:xue yi yang
import requests
url = "https://music.163.com/weapi/song/enhance/player/url/v1?csrf_token=0df946aef156e37218af8fec3a7295c9"
headers = {
    "Content-Type":"application/x-www-form-urlencoded",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36"
}
data = "params=tJsxRBktm22%2FOjFOLzGH1sYOvr672q17IPL46ZLVy%2B%2FJJf3rmmGYCRilfKIIKRvrLJ%2ByAFi%2FOOms4btnEaVyWMnIZqYbyEIpZFDDhlR4%2BRpdOD8En2mdVsVoiFGZHufivD9OXFqPv6Wcl3m7%2B5JDFtH%2BegtevU55X0O5%2BTBcYni8Wo%2Fu8yx%2FWPsS43tiGUnUuVTlSXnZ0%2FEDc0zC%2FU2aAw%3D%3D&encSecKey=24cbf34a75f7c83d3aca955e8a4c91941c8818c3683edb91e8fb193db63ab22224f7c4c9983c5afb916035badd4fb5f7783e9e8f6bd0d4315270a4d9a253deac56cc6fe17e816de246b6526575a94a43bb925299961e54786607849d125d249c9e376e64b86850bb7cffb70e28a0043fd69979f43024c07b9b9f32599c97991b"
res = requests.post(url=url,data=data,headers=headers).text
print(res)