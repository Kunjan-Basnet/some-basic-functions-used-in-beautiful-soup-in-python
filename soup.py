from bs4 import BeautifulSoup
import re

with open("index.html") as fp:
    soup=BeautifulSoup(fp,"html.parser")
    # print(soup.title)
    # print(soup.prettify())
    # print(soup.title.name)
    # print(soup.head.string)
    # print(soup.p["class"])
    # elem=soup.find(id="link1")
    # print(elem)
    # print(soup.find_all("a"))
    # for link in soup.find_all("a"):
    #     print(link.get("href"))
    # print(soup.get_text())
    # print(soup.title.get_text())
    # print(soup.a.attrs)
    # print(soup.p['class'])
    # soup.p['class']="untitled" #attributes inside a tag can be manipulated as python dictionary
    # print(soup.p['class'])
    # soup.p["another_attribute"]=1
    # print(soup.p)
    # soup.a["class"]=["sister","mister"]
    # print(soup.a["class"])
    # print(soup.a.get_attribute_list("class"))
    # print(soup.a)
    # print(soup.head.contents)
    # for stri in soup.stripped_strings:
    #     print(stri) 
    # for child in soup.html.descendants:
    #     print(child)
    # print(soup.title.parent)
    # print(soup.find_all(class_=re.compile("sister"))) #using regular expression re
    # print(soup.find_all(string=re.compile("Dormouse")))
    # print(soup.css.select("title"))
    # print(soup.css.select("#link1"))
    # print(soup.css.select("body a"))
    # list=[]
    list=soup.find_all("a",class_=re.compile("sister"))
    print(list)
    # print(soup.get_text(separator="\n"))