import openai
import requests
import os
from bs4 import BeautifulSoup
from dotenv import load_dotenv


load_dotenv()
key =os.environ['WEB_API_KEY']
# Set OpenAI API key
openai.api_key = key

def WriteSummary(content):
    #this function asks ChatGPT to follow the prompt of the inserted content from the function call.
    prompt= f"Write a summary about the following article in 50 words or less: {content}"
    summary=openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role":"user", "content":prompt}])
    return summary.choices[0].message.content                                                                       #this returns the summary that the ai has made 

def OutputToFile(idx,title,summary):
    #this prints the summary and title to the ai_gen folder with all of the output files.
    with open(f'Data/ai_gen/output_{idx}.txt', 'w') as output_file:                                 
        output_file.write(f"Title: {title}\nSummary: {summary}")


def performAction():
    #this is the over-lying function that runs the program. It opens the urls to scrape the article and then indexes through each line and calls the output function
    with open('urls.txt', 'r') as file:
            urls = file.readlines()
    for idx, url in enumerate(urls):
            response = requests.get(url.strip())
            soup = BeautifulSoup(response.content, 'html.parser')
            title = soup.find('title').get_text()                   #collects article title
            try:                                                    #attempts to get the article and put it into content
                content = soup.find('article').get_text()
            except:
                content = "There was no article in this "
            #there is no safeguard to make sure that an article is suitable this time, it is expected that only good articles are collected. If not, there is not going to be a summary for the article
            #video articles do not work, if you look at the example output #2, I included that as an extra to show that.
            OutputToFile(idx,title,WriteSummary(content))                  #passing in the idx title, and function(that will return the summary) allows for the file name to be indexed and the title and summary to be passed through.
