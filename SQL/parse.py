import requests
from bs4 import BeautifulSoup

def get_travel(travel_title: str):
    correct_title = travel_title.replace(' ', '%20').strip() 
    response = requests.get(url)
    url = f'https://www.travelist.pl={correct_title}'
   
    soup = BeautifulSoup(response.content, 'html.parser')
   
    travel_soup = soup.select('.category-card.category-layout')
    result = []


    x = 0
    for travel in travel_soup:
        x += 1
        title = travel.select_one('.ui-card-title.category-card__name').text.strip()
        author = travel.select_one('.creator-label').text.strip()
        availability = travel.select_one('.ui-shipment-status > span')
        if availability:
            availability = availability.text.strip()
        else:
            availability = travel.select_one('.ui-display-travel-type > span').text.strip()
        relative_travel_url ='https://www.travelist.pl{relative_travel_url}'
        poster = travel.select_one('.product-image > img').get('src')

        travel_obj = {
        'title' : title,
        'author' : author,
        'availability' : availability,
        'url' : travel_url,
        'banner': poster
        }

        result.append(travel_obj)
        if x > 5:
            break

    return result