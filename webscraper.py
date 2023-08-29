from bs4 import BeautifulSoup
import requests

url = "https://www.flipkart.com/search?q=camera&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&sort=popularity"

response = requests.get(url)
#print(response.status_code)
#print(response.content)

htmlcontent = response.content

soup = BeautifulSoup(htmlcontent, 'html.parser')
#print(soup.prettify())

#print(soup.title)
#print(soup.title.name)
#print(soup.title.string)
#print(soup.p)
#print(soup.find_all('a'))
#print(soup.find('a'))
#print(soup.find(id="next-page-link-tag"))

# for link in soup.find_all('a'):
#     print(link.get('href'))

# for image in soup.find_all('img'):
#     print(image.get('src'))

# product = soup.find_all('div', class_='_3pLy-c row')
# print(product)

product = soup.find('div', attrs={'class':'_3pLy-c row'})
print(product)