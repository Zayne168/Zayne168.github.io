
## Zayne Bonner

# My Scrapper
This software will scrape as many urls as there are in 'urls.txt' of there data and use BeautifulSoup and OpenAI API to scrape articles. There are three modules, a verifier, a manual scraper, and a ChatGPT based Scraper. The verifer is used for the manual scraper to determine which links are valid to be scraped and which ones are not. The manual scraper module(module 2) scrapes the verified urls in both a raw and processed format. The AI Scraper is independent and attempts to scrape each url no matter the validity.

# The set up
1. it is assumed that all of the program files are downloaded 
2. Set up the conda environment. We are going to assume Conda is installed for this. in your terminal, please type: conda create --name *PreferredEnvName* --file requirement.yaml 
3. you can name it whatever you like in the above code.
4. This creates the environment from the provided requirement.yaml file in this folder.
5. Next, type in "conda activate " followed by your decided environment name from above.
6. Once this is done, we can use the included python package in the environment
7. In the urls.txt file, you can paste as many official news articles as you want. please stay away from video based articles as they are weird, I have provided one already to show that.
8. make sure each URL is on its own line, all of the scrapers work by indexing off of each new line.
9. do the API set up below 
10. Once you have your articles, you can type "python run.py" in your terminal with the active environment in order to scrape them.
11. if you would like, you can modify the run.py file to only include the specific types of scrapers you want. You can utilize any of the API-based, raw, or manual processed scrapers by commenting out the ones you do not want.



# OpenAI API Account Setup

Creating an OpenAI API and API Key

## Step 1: Create an OpenAI Account

1. Go to the [OpenAI website](https://openai.com).
2. Click on "Sign Up"
3. Fill in the required information

## Step 2: Generating an API Key

1. Log in to your OpenAI account if you're not already logged in.
2. Navigate to the "API" section or click on "API" in the top menu.
3. Look for the option to generate an API key. It might be labeled as "Generate API Key" or something similar.
4. Click on the "Generate API Key" button.
5. Your API key will be displayed on the screen. Copy this key and store it securely. You can not view it later

## Step 3: using api key in our program

1. Back to this program. in your local version of this program repository, make a file called ".env"
2. in this file paste "WEB_API_KEY='-your API key you generated above here- '"
3. your run.py should then work


# Test Cases
This project is an extension of Project 3 with Jack W. We added 8 total test cases to ensure our program runs fluidly each time and to catch and alert the user of any mal-use. 
1.  We test whether each url has a ".com" which would indicate if a url is valid,
2.  test whether there is a url file at all,
3.  test whether the ai makes a <50 word summary or if its too long,
4.  test whether each article has a title,
5.  test whether each article has content to be summarized,
6.  test whether there is an API key to be taken in,
7.  test that there is the correct number of output files comparative to the amount of URLS in urls.txt,
8.  and we test whether the system is outputting at all. 
