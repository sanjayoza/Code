# Scrape data into CSV file
# Goal: Grab all the links from Rithm School Blog
# Data: store URL, anchor tag text, data
# use chrome to look at the developer tools to understand tags.

import requests
from bs4 import BeautifulSoup
from csv import writer

url = "https://www.rithmschool.com/blog"

response = requests.get(url)
#print(response.text)           # html data

# instantiate BeautifulSoup

soup = BeautifulSoup(response.text, "html.parser")
#print(soup.text)

# select all articles
articles = soup.find_all("article")
#print(articles)

with open("blogdata.csv", "w") as file:
    csv_write = writer(file)
    csv_write.writerow(["Title", "Link","Data"])    # write header row
    # for an article look for anchor tag a and print the text from it.
    for article in articles:
        a_tag = article.find("a")
        # get the title
        title = a_tag.get_text()
        print(title)
        
        # get the href/url for the article
        href = a_tag.attrs['href']   # if only attrs is used then a dictionary is returned
        print(href)
        
        adate = article.find("time").attrs['datetime']
        # or you can do 
        #adate = article.find("time")['datetime']
        print(adate)
        csv_write.writerow([title, href, adate])
    
    
    
    
    