
import requests
from bs4 import BeautifulSoup

url = "https://www.crummy.com/software/BeautifulSoup/bs4/doc/"
webpage1 = requests.get(url)
bs = BeautifulSoup(webpage1.content,"html.parser")
elements = bs.find_all(class_='align-right')

# Print the results
for element in elements:
    print(element.prettify())
print(elements)

imgs = bs.select("img")

# Print the results
for img in imgs:
    src_url= str(img.get("src"))
    print(src_url)
    img_url = url+src_url
    print("img url is :",img_url)
    response = requests.get(img_url)
    response.raise_for_status()
    imgname= img_url.split("/")[-1]



    with open(imgname,'wb') as File:
        File.write(response.content) 
