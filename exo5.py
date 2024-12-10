import requests
from bs4 import BeautifulSoup

webpage1 = requests.get(' http://universities.hipolabs.com/search?country=Algeria')
print(webpage1.json())

webpage2=requests.get( ' https://www.licbplus.com.dz/global-category/laptop-computers/3/225?sort_by=new')
bs = BeautifulSoup(webpage2.content,"html.parser")
laptops_names= bs.select('div.product-content-wrap h2')
laptops_prices= bs.select('div.product-content-wrap div.product-card-bottom span')
print('laptops names')
print([div.text for div in laptops_names])

print('laptops prices')
print([div.text for div in laptops_prices])

