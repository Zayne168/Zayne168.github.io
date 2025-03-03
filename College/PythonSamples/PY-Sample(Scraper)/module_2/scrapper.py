import requests
from bs4 import BeautifulSoup

#This has 2 scrap functions for the raw and processed outputs
#raw outputs everything that the article got completely unfiltered
#neat outputs the title and synopsis/description of each article
#the verified array talked about earlier is utilized in an if statement to decide whether a file is worthy of an output
#
class MyScrapper:
    def ScrapRaw(verified):
        with open('urls.txt', 'r') as file:
            urls = file.readlines()
        for idx, url in enumerate(urls):
            response = requests.get(url.strip())
            soup = BeautifulSoup(response.content, 'html.parser')
            try:
                content = soup.find('article').get_text()
            except:
                content = "scrapper could not find article"
            if(bool(verified[idx])):
                with open(f'Data/raw/output_{idx}.txt', 'w') as output_file:
                    output_file.write(content)

    def ScrapNeat(verified):   
        with open('urls.txt', 'r') as file:
            urls = file.readlines()
        for idx, url in enumerate(urls): 
            response = requests.get(url.strip())
            soup = BeautifulSoup(response.content, 'html.parser')
            if(bool(verified[idx])):
                title = soup.find('title').get_text()                                           
                synopsis = soup.find('meta', attrs={'name': 'description'})['content']                                                                         
                with open(f'Data/processed/output_{idx}.txt', 'w') as output_file:                                 
                    output_file.write(f"Title: {title}\nSynopsis: {synopsis}")