import requests
import re
from lxml.html import soupparser
from bs4 import BeautifulSoup
headers = {'User-Agent': 'Mozilla/5.0'}
url = "https://www.fundoodata.com/companies-detail/A-G-N-Software-Consultants/51421.html?&pageno=2"
r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.text, "lxml")
name = soup.find("div", attrs = {'class':'search-page-heading-red'}).text
phonenum = soup.find("img", attrs = {'src':'images/call.png'}).next_sibling
addressp1 = soup.find(text = 'Address').parent.next_sibling
addressp2 = soup.find(text = 'Address').parent.next_sibling.next_sibling.next_sibling
address = addressp1 + " " + addressp2
address = " ".join(address.split())
industry = soup.find(text = 'Industry').parent.next_sibling.next_sibling
companytype = soup.find(text = 'Company Type').parent.next_sibling.next_sibling
print("Name "+name)
print("Phone Number "+phonenum)
print("Address " + address)
print("Industry " + industry)
print("Company Type " + companytype)

