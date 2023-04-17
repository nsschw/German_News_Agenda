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
            dict_article = {"header": "", "subheader": "", "type": "", "meta": ""}
            
            #for the main articles
            header_element = article.css('.zon-teaser-classic__faux-link')
            if header_element:
                dict_article["header"] = header_element[0].text()
                dict_article["type"] = "main"
            subheader_element = article.css('.zon-teaser-classic__text') 
            if subheader_element:
                dict_article["subheader"] = subheader_element[0].text()
            meta_element = article.css('.zon-teaser-classic__metadata')
            if meta_element:
                dict_article["meta"] = meta_element[0].text()     

            #for the lead articles
            header_element = article.css('.zon-teaser-lead__faux-link')
            if header_element:
                dict_article["header"] = header_element[0].text()
                dict_article["type"] = "lead"
            subheader_element = article.css('.zon-teaser-lead__text') 
            if subheader_element:
                dict_article["subheader"] = subheader_element[0].text()
            meta_element = article.css('.zon-teaser-lead__metadata')
            if meta_element:
                dict_article["meta"] = meta_element[0].text()    

            #for the regular articles
            header_element = article.css('.zon-teaser-standard__faux-link')
            if header_element:
                dict_article["header"] = header_element[0].text()              
            subheader_element = article.css('.zon-teaser-standard__text')
            if subheader_element:
                dict_article["subheader"] = subheader_element[0].text()
                dict_article["type"] = "regular"
            meta_element = article.css('.zon-teaser-standard__metadata')
            if meta_element:
                dict_article["meta"] = meta_element[0].text()

            #for the wide articles
            header_element = article.css('.zon-teaser-wide__faux-link')
            if header_element:
                dict_article["header"] = header_element[0].text()              
            subheader_element = article.css('.zon-teaser-wide__text')
            if subheader_element:
                dict_article["subheader"] = subheader_element[0].text()
                dict_article["type"] = "wide"
            meta_element = article.css('.zon-teaser-wide__metadata')
            if meta_element:
                dict_article["meta"] = meta_element[0].text()


            if dict_article["header"] != "":
                #save in homepage dict
                dict_homepage["articles"].append(dict_article)


        #Append to list of homepages
        list_homepages.append(dict_homepage)


    #save in json file
    if not os.path.exists("Data/All"):
        os.mkdir("Data/All") 
    with open("Data/All/zeit.jsonl", "w", encoding="utf-8") as f:
        json.dump(list_homepages, f, indent=2) 



def save_welt_as_json(homepages):
    list_homepages = []    

    for homepage in homepages:        
        dict_homepage = {"timestamp": homepage[0], "articles": []}
        html = homepage[1]
        html = HTMLParser(html)
        articles = html.css('article')

        for article in articles:           
            #variables            
            dict_article = {"topic": "", "header": "", "subheader": "", "type": "", "meta": ""}


            #for the main articles
            teaser_element = article.css('.o-teaser__topic')
            if teaser_element:
               dict_article["topic"] = teaser_element[0].text()

            headline_element = article.css('.o-headline')
            if headline_element:
                dict_article["header"] = headline_element[0].text()

            text_element = article.css('.o-text')
            if text_element:
                dict_article["subheader"] = text_element[0].text()


            if dict_article["header"] != "":
                    #save in homepage dict
                    dict_homepage["articles"].append(dict_article) 
        
        #Append to list of homepages
        list_homepages.append(dict_homepage)
    
    #save in json file
    if not os.path.exists("Data/All"):
        os.mkdir("Data/All") 
    with open("Data/All/welt.jsonl", "w", encoding="utf-8") as f:
        json.dump(list_homepages, f, indent=2) 




if __name__ == "__main__":
    zeit = read_files("zeit")
    save_zeit_as_json(zeit)

    welt = read_files("welt")
    save_welt_as_json(welt)
    