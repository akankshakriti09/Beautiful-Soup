from bs4 import BeautifulSoup
import requests

url = "https://www.flipkart.com/search?q=camera&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&sort=popularity"

response = requests.get(url)

htmlcontent = response.content

soup = BeautifulSoup(htmlcontent, 'html.parser')

titles = []
prices = []
images = []

for d in soup.find_all('div', attrs={'class':'_2kHMtA'}):
    title = d.find('div', attrs={'class':'_4rR01T'})
    #print(title)
    #print(title.string)

    price = d.find('div', attrs={'class':'30jeq3 _1_WHN1'})
    #print(price.string)

    image = d.find('img', attrs={'class':'_396cs4 _3exPp9'})
    #print(image.get('src'))

    titles.append(title.string)
    prices.append(price.string)
    images.append(image.get('src'))

    #print(titles)
    print(prices)