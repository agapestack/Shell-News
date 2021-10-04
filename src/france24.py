from bs4 import BeautifulSoup
import requests
import json

headers = {
    "User-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36"}
url = "https://www.france24.com/fr/"
htmlFilePath = "./tmp/html/fr24.html"
jsonFilePath = "./tmp/json/fr24.html"

tmp_data = {}
tmp_data['article'] = []


def getHtmlFile(htmlFilePath, url, headers):
    res = requests.get(url, headers=headers)
    file = open(htmlFilePath, "w+")
    file.write(res.text)
    file.close()


def getArticleFromFile(htmlFilePath, jsonFilePath, url, headers):
    getHtmlFile(htmlFilePath, url, headers)

    htmlFile = open(htmlFilePath, "r")
    soup = BeautifulSoup(htmlFile, "html.parser")
    news = soup.find_all("div", {"class": "m-item-list-article"})

    for i in range(min(len(news), 20)):
        article = {}
        article['title'] = news[i].find("p", {"class": "article__title"})
        # article['article_link'] =
        # article['img_link'] =  
        print(str(i+1) + "/ " + article['title'].text)

    htmlFile.close()

    jsonFile = open(jsonFilePath, "w+")
    json.dump(tmp_data, jsonFile)
    jsonFile.close()

getArticleFromFile(htmlFilePath, jsonFilePath, url, headers)
