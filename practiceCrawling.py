import requests
from bs4 import BeautifulSoup

url = "https://www.youtube.com/feed/trending?bp=6gQJRkVleHBsb3Jl"
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"} 
response = requests.get(url, headers=header)
response.raise_for_status()

soup = BeautifulSoup(response.text, "lxml")
arr = soup.select("#grid-container > ytd-video-renderer")
print(len(arr))
for i in arr:
    print(i.get_text())