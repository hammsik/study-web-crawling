import requests
from bs4 import BeautifulSoup

url = "https://maplestory.nexon.com/N23Ranking/World/Total"
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"} 
response = requests.get(url, headers=header)
response.raise_for_status()

soup = BeautifulSoup(response.text, "lxml")
# print(response.text)
arr = soup.select("#container > div > div > div:nth-child(4) > div.rank_table_wrap > table > tbody > tr > td > dl")
for i in arr:
    print(i.a.get_text() + " " + "https://maplestory.nexon.com/" + i.a["href"] + "\n")
# with open("메이플.html", "w", encoding="utf-8") as crawling:
#     crawling.write(response.text)