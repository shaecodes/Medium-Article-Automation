from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import pandas as pd


website = "https://medium.com/" #website that is being scraped
path = "/Users/sincl/Downloads/chromedriver_win32/chromedriver.exe" #location of chromedriver

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)
driver.get(website)

time.sleep(5) #delay so that most of the articles load

articles = driver.find_elements(by="xpath", value='//div[@class="eo ak ay ag"]') #list with all the articles

#initialization of lists to store the titles, subtitles and links
titles = []
subtitles = []
links = []

#adds articles, subtitles and link to their respective list
for article in articles:
    title = article.find_element(by="xpath", value='./a/h2').text
    subtitle = article.find_element(by="xpath", value='./a/div').text
    link = article.find_element(by="xpath", value='./a').get_attribute("href")

    titles.append(title)
    subtitles.append(subtitle)
    links.append(link)

#heading do csv file
my_dict = {'Title': titles, 'Subtitle': subtitles, 'Link': links}

# convert the dictionary to a pandas dataFrame
med_headlines = pd.DataFrame(my_dict)

# save the dataFrame to a csv file
med_headlines.to_csv('medium.csv')

driver.quit()