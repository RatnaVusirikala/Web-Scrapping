from bs4 import BeautifulSoup
import requests
import datetime
from selenium import webdriver

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
url = "https://www.bensbites.co/"
req = requests.get(url, headers=headers)
soup = BeautifulSoup(req.text, "html.parser")
results = soup.find("div", attrs={'class':'flex flex-col divide-y sm:divide-none'})

job_elements = results.find_all("a", class_="group relative flex grid w-full grid-cols-1 gap-x-8 gap-y-4 transition-all sm:my-6 sm:grid-cols-2 sm:gap-y-6 sm:gap-x-6 flex-row mb-6 gap-y-0 sm:mb-0")
timeList = soup.findAll('time')
count = 0

for job_element in job_elements:
    title_element = job_element.find("h2", class_="line-clamp-2 wt-header-font text-wt-text-on-background text-xl sm:text-2xl font-bold")
    subtitle_element = job_element.find("p", class_="font-regular mb-2 opacity-75 wt-header-font line-clamp-4 text-wt-text-on-background text-md sm:text-lg font-regular")

    reference_element = job_element.find("div",class_="absolute inset-0 z-0 -m-4 rounded-wt bg-transparent transition duration-200 sm:-m-6 group-hover:bg-slate-100/50")
    parent_element = reference_element.parent

    Time = timeList[count]['datetime'].split('T')[0]
    count +=1
    
    print('Title - ' + title_element.text)
    print('Sub_Title - ' + subtitle_element.text.removeprefix('PLUS: '))
    print('Link - ' + "https://www.bensbites.co" + parent_element['href'])
    print('Time - ' + Time)
    print('Image - ' + job_element.find('img')['src'])
    print()
