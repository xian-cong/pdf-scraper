import os
import requests
import shutil
from urllib.parse import urljoin
from bs4 import BeautifulSoup

url = "https://www.savemyexams.co.uk/igcse-physics-cie-new/topic-questions-2/#tab-a1db719133c2e0694bd"

#If there is no such folder, the script will create one automatically
folder_location = r'C:\Users\User\Desktop'
if not os.path.exists(folder_location):os.mkdir(folder_location)

response = requests.get(url)
soup= BeautifulSoup(response.text, "html.parser")     
for link in soup.select("a[href$='.pdf']"):
    #Name the pdf files using the last portion of each link which are unique in this case
    filename = os.path.join(folder_location,link['href'].split('/')[-1])
    with open(filename, 'wb') as f:
        f.write(requests.get(urljoin(url,link['href'])).content)

if os.path.exists("C:\Users\User\Desktop\webscraping/329239-2018-2019-syllabus.pdf"):
  os.remove("C:\Users\User\Desktop\webscraping/329239-2018-2019-syllabus.pdf") # one file at a time
if os.path.exists("C:\Users\User\Desktop\webscraping/CIE-IGCSE-Physics-0625_0972-Past-Paper-Checklist.pdf"):
  os.remove("C:\Users\User\Desktop\webscraping/CIE-IGCSE-Physics-0625_0972-Past-Paper-Checklist.pdf") # one file at a time
if os.path.exists("C:\Users\User\Desktop\webscraping/CIE-IGCSE-Physics-Topic-Checklist.pdf"):
  os.remove("C:\Users\User\Desktop\webscraping/CIE-IGCSE-Physics-Topic-Checklist.pdf") # one file at a time
