import hashlib
import requests, socket
from requests.exceptions import ConnectionError
data = requests.get("https://money.cnn.com/data/markets/dow").text
price = data.split('<td>Open</td><td class="wsod_quoteDataPoint">')[1].split("<")[0]
hsh = hashlib.md5(price.encode("ascii")).hexdigest()
def towords(code):
    words=["base", "rest", "lesson", "tidy", "harass", "shop", "miner", "dozen", "spoil", "revoke", "gem", "pack", "attack", "script", "volume", "glass"]
    output=""
    for x in code:
        output+=words[int(x, 16)]+"-"
    output=output[:-1]
    return output
for i in range(1000):
    url = towords(hsh[:8])+".org"
    print("checking",url)
    try:
        socket.gethostbyname(url)
        if requests.head("http://"+url).status_code<400:
            print("Active domain found!")
    except (ConnectionError, socket.gaierror):
        pass
    hsh = hashlib.md5(hsh.encode("ascii")).hexdigest()
