import requests
from bs4 import BeautifulSoup
import sys


#This is a simple try->except module/function that creates a verification array
#that correlates to my urls array and states whether a url is valid for output or not
#run.py saves this and passes it into scrap four output prep
#if there is any troubles it will throw the user an understandable error so that they can fix
#the problem with the url list they provided
#I included 3 'bad' links in my sample url list so that this is shown in testing


verified=[]

def Verify():
    with open('urls.txt', 'r') as file:
        urls = file.readlines()
    for idx, url in enumerate(urls):
            try:
                response = requests.get(url.strip())
                soup = BeautifulSoup(response.content, 'html.parser')
            except:
                print("invalid URL on line "+str(idx+1)+" of urls.txt.")
                print("Fix this and re-run the program.")
                sys.exit()
            try:
                title = soup.find('title').get_text() 
                content = soup.find('article').get_text()                                          
                synopsis = soup.find('meta', attrs={'name': 'description'})['content']
                verified.append(True)
                
            except:
                print(f"Could not find some or all of: title, article, or synopsis in {url}, this link has been skipped\n")
                verified.append(False)
            