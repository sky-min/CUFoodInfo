import requests
from bs4 import BeautifulSoup  

nutrient = [] 
name = [] 

for page in range(0, 143): 
	news_url = 'https://mobile.fatsecret.kr/%EC%B9%BC%EB%A1%9C%EB%A6%AC-%EC%98%81%EC%96%91%EC%86%8C/search?q=CU&pg=' + str(page) 
	raw = requests.get(news_url) 
	
	soup = BeautifulSoup(raw.text, 'html.parser') 
	
	box = soup.find('table', {'class' : 'list'}) 
	all_nu = box.find_all('div', {'class': 'nowrap small-text'}) 
	all_name = box.find_all('a',{'class':'inner-link'}) 
	
	for nutri in all_nu: 
		n = nutri.text 
		nutrient.append(n.strip()) 
		
	for i in range(0, len(all_name), 2):
		nam = all_name[i].text
		name.append(nam.strip()) 
		
무게 = []
칼로리 = []
지방 = [] 
탄수화물 = [] 
단백질 = [] 

for i in range(len(nutrient)): 
	gram = nutrient[i].split('-')[0].strip() 
	
	b = nutrient[i].split('-')[1].split('|') 
	cal = b[0].split(':')[1].strip() 
	fat = b[1].split(':')[1].strip() 
	carbo = b[2].split(':')[1].strip() 
	protein = b[3].split(':')[1].strip() 
	
	무게.append(gram) 
	칼로리.append(cal) 
	지방.append(fat) 
	탄수화물.append(carbo) 
	단백질.append(protein) 

import pandas as pd

CU = pd.DataFrame([x for x in zip(name, 무게, 칼로리, 지방, 탄수화물, 단백질)])
CU.columns = ['상품이름','무게','칼로리','지방','탄수화물','단백질']
CU.to_csv('CU.csv',encoding='cp949')