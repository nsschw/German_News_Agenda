import requests
import json
import os
import datetime


def download(url, newspaper):

    if not os.path.exists("Data"):
        os.mkdir("Data")    
    if not os.path.exists(f"Data/{newspaper}"):
        os.mkdir(f"Data/{newspaper}")

    response = requests.get(url)   

    if response.status_code == 200:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")        
        with open(f"Data/{newspaper}/{timestamp}.html", "w", encoding="utf-8") as f:
            f.write(response.text)


if __name__ == "__main__":

    download("https://www.bild.de/", "bild")
    download("https://welt.de", "welt")
    download("https://www.faz.net/aktuell/", "faz")
    download("https://www.taz.de/", "taz")
    download("https://www.wz.de/", "westdeutsche")
    download("https://www.sueddeutsche.de/", "sz")
    download("https://www.zeit.de/", "zeit")
    download("https://www.spiegel.de/", "spiegel") 
    download("https://www.tagesschau.de/", "tagesschau")
    download("https://www.handelsblatt.com/", "handelsblatt")
    download("https://www.nd-aktuell.de/", "neue-deutsche")
    download("https://www.freitag.de/", "freitag")
    download("https://tagesspiegel.de", "tagesspiegel")
    download("https://www.fr.de/", "fr")
    download("https://jungefreiheit.de/", "jungefreiheit")
    download("https://www.jungewelt.de/", "jungewelt")
    download("https://www.merkur.de/", "merkur")
    download("https://www.n-tv.de/", "ntv")
    download("https://rp-online.de/", "rponline")