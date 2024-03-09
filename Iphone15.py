from urllib import request
from urllib.request import Request
from bs4 import BeautifulSoup
import json

url = 'https://www.flipkart.com/apple-iphone-15-pink-128-gb/product-reviews/itm7579ed94ca647?pid=MOBGTAGPNMZA5PU5&lid=LSTMOBGTAGPNMZA5PU5O32WJC&marketplace=FLIPKART'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Referer": "https://www.flipkart.com/"
}
iphones=[]
for page in range(1, 21):
    page_url = f'{url}&page={page}'

    request_site = Request(page_url, headers=headers)
    html = request.urlopen(request_site)
    soup = BeautifulSoup(html, 'html.parser')

    Customer_name = [name.text for name in soup.find_all('p', {'class': '_2sc7ZR _2V5EHH'})]
    ratings = [rating.text for rating in soup.find_all('div', {'class': '_3LWZlK _1BLPMq'})]
    reviews = soup.find_all('div', {'class': 't-ZTKy'})

    # Removing 'Read More' from reviews
    for review in reviews:
        read_more = review.find('span', {'class': '_1H-bmy'})
        if read_more:
            read_more.decompose()

    review_texts = [review.get_text() for review in reviews]

    for name,rating,reviews in  zip(Customer_name, ratings, review_texts):
        iphone_info = {
            'Buyer_name':name,
            'Rating':rating,
            'Review':reviews
        }
        iphones.append(iphone_info)
jsonfile = open("Iphone15.json","w")
json.dump(iphones,jsonfile)
