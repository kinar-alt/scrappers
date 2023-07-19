

from bs4 import BeautifulSoup
import requests
import pandas as pd


# %%
# Main Scrapper
# london_id=1233135775

city_id = 1233135775
main_df = pd.DataFrame()
try:
    for i in range(10, 500, 10):
        main_content_soup = BeautifulSoup(requests.get(
            f'https://www.spareroom.co.uk/flatshare/?offset={i}&search_id={city_id}&sort_by=by_day&mode=list', verify=False).text, features="lxml").find("ul", attrs={"class": "listing-results"})

        list_of_content = main_content_soup.findAll(
            "li", attrs={"class": "listing-result"})

        detail_urls = [lo.a['data-detail-url'] for lo in list_of_content]
        tiltle_properties = [lo.a['title'] for lo in list_of_content]
        href_properties = [lo.a['href'] for lo in list_of_content]
        desc = [
            lo.find("p", attrs={"class": "description"}).text for lo in list_of_content]
        listingPrice = [lo.find(
            "strong", attrs={"class": "listingPrice"}).text for lo in list_of_content]
        shortDescription = [lo.find(
            "em", attrs={"class": "shortDescription"}).text for lo in list_of_content]
        listingLocation = [lo.find(
            "span", attrs={"class": "listingLocation"}).text for lo in list_of_content]

        listing_equiv_room_price = [lo.find("span", attrs={"class": "listing_equiv_room_price"}).text if lo.find(
            "span", attrs={"class": "listing_equiv_room_price"}) else "Not-Given" for lo in list_of_content]
        freeToContact = [lo.find("span", attrs={"class": "freeContact status"}).text if lo.find(
            "span", attrs={"class": "freeContact status"}) else 'Not-Given' for lo in list_of_content]

        df = pd.DataFrame({

            'tiltle_properties': tiltle_properties,
            'listingLocation': listingLocation,
            'description': desc,
            'shortDescription': shortDescription,
            'listingPrice': listingPrice,
            'href_properties': href_properties,
            'detail_urls': detail_urls,
            'listing_equiv_room_price': listing_equiv_room_price,
            'freeToContact': freeToContact
        })
        main_df = pd.concat([df, main_df], axis=0)

except:
    print('NOTTTT')


