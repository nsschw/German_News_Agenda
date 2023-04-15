import os
from selectolax.parser import HTMLParser
import json


#read in the files
def read_files(folder):
    articles = []
    files = os.listdir(f"Data/{folder}")
    for file in files:
        with open(f"Data/{folder}/{file}", "r", encoding="utf-8") as f:
            articles.append((file.split(".")[0], f.read()))
    return articles



def save_zeit_as_json(homepages):

    list_homepages = []    

    for homepage in homepages:        
        dict_homepage = {"timestamp": homepage[0], "articles": []}
        html = homepage[1]
        html = HTMLParser(html)
        articles = html.css('article')

        for article in articles:           
            #variables            
            dict_article = {"header": "", "subheader": "", "is_main_article": False}
            

            #for the main article
            header_element = article.css('.zon-teaser-classic__faux-link')
            if header_element:
                dict_article["header"] = header_element[0].text()
                dict_article["is_main_article"] = True

            subheader_element = article.css('.zon-teaser-classic__text') 
            if subheader_element:
                dict_article["subheader"] = subheader_element[0].text()              


            #for the regular articles
            header_element = article.css('.zon-teaser-standard__faux-link')
            if header_element:
                dict_article["header"] = header_element[0].text()                
            
            subheader_element = article.css('.zon-teaser-standard__text')
            if subheader_element:
                dict_article["subheader"] = subheader_element[0].text()


            #save in homepage dict
            dict_homepage["articles"].append(dict_article)

        list_homepages.append(dict_homepage)

    with open("Data/zeit/zeit.jsonl", "w", encoding="utf-8") as f:
        json.dump(list_homepages, f, indent=2)
    
    
                
 



if __name__ == "__main__":
    x = read_files("zeit")
    save_zeit_as_json(x)
    