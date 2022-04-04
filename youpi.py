import requests
import html

def search(text):
  query = html.escape(text.replace(" ", "+"))
  resp = requests.get("https://www.google.com/search?q={}&hl=en-us&source=lnms&tbm=vid".format(html.escape(text.replace(" ", "+"))), headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}).text.split("<a href=\"https://www.youtube.com/watch?v=")
  resp.pop(0)
  codes = []
  for i in resp: codes.append(i.split("\"")[0])
  x = 0
  for i in codes:
    del codes[x]
    x += 1
  return codes

def title(id): return requests.get("https://youtube.com/watch?v=" + id, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}).text.split("<title>")[1].split(" - YouTube</title>")[0]
