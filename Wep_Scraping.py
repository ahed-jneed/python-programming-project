import requests
from bs4 import BeautifulSoup 
import csv 
from itertools import zip_longest

from requests.models import Response, get_cookie_header 
Job_Titles = []
Company_Name = []
Location_Name = []
Job_Skills = []
Links = []
Salarys = []
Responsibilities = []
Date = []
page_num = 0
while True:
    try:
        result = requests.get(f"https://wuzzuf.net/search/jobs/?a=spbl&q=python&start={page_num}")
        src = result.content 

        soup = BeautifulSoup(src,"lxml")
        page_limit = int(soup.find("strong").text)
        if (page_num > page_limit // 15):
            print("Pages ended,terminate")
            break
        job_titles = soup.find_all("h2",{"class":"css-m604qf"})
        company_name = soup.find_all("a",{"class":"css-17s97q8"})
        location_name = soup.find_all("span",{"class":"css-5wys0k"})
        job_skills = soup.find_all("div",{"class":"css-y4udm8"})
        posted_new = soup.find_all("div",{"class":"css-4c4ojb"})
        posted_old = soup.find_all("div",{"class":"css-do6t5g"})
        posted = [*posted_new,*posted_old]

        for i in range(len(job_titles)):
            Job_Titles.append(job_titles[i].text)
            Company_Name.append(company_name[i].text)
            Location_Name.append(location_name[i].text)
            Job_Skills.append(job_skills[i].text)
            Links.append(job_titles[i].find("a").attrs['href'])
            date_text = posted[i].text.replace("-","").strip()
            Date.append(posted[i].text)
        page_num += 1
        print("Page switched")
    except:
            print("error")
            break
for link in Links:
    result = requests.get(link)
    src = result.content
    soup = BeautifulSoup(src,'lxml')
    salary = soup.find("div",{"class":"matching-requirement-icon-container","data-toggle":"tooltip","data-placement":"top"})
    Salarys.append(salary.text.strip())
    requirements = soup.find("span",{"itemprop":"responsibilities"}).ul
    respon_text = ""
    for li in requirements.find_all("li"):
     respon_text += li.text+"# "
     respon_text = respon_text[:-2]
     Responsibilities.append(respon_text)


file_list =[Job_Titles,Company_Name,Date,Location_Name,Job_Skills,Links,Salarys,Responsibilities]
exported = zip_longest(*file_list)
with open("/Users/hp/python project/c.csv","w") as myfile:
    wr = csv.writer(myfile)
    myfile.columns = wr.writerow(["Job titles","Company name","Date","Locatin name","Job skills","Links""Salarys","Responsibilities"]) 
    wr.writerows(exported)


