import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

# URL of the webpage to scrape
catalog_url = "https://www.sokolin.com/sitemap"

# Fetch the webpage content

def fetch_page(url):
    response = requests.get(url)
    response.raise_for_status()  # Will raise an error for bad status
    return BeautifulSoup(response.text, 'html.parser')
# response = requests.get(url)
# webpage = response.text
# Parse the HTML content
# soup = BeautifulSoup(webpage, 'html.parser')

def scrape_links(page_soup):
    links = page_soup.find_all('a')  # Find all anchor tags
    return [link.get('href') for link in links if link.get('href')]



catalog_soup = fetch_page(catalog_url)

sitemap_links = scrape_links(catalog_soup)

for page_url in sitemap_links:
    try:
        # Fetch and parse each page
        page_soup = fetch_page(page_url)

        # Scrape links from the page
        page_links = scrape_links(page_soup)

        # Process the links (print them, store them, etc.)
        for link in page_links:
            if link.startswith("https://www.sokolin.com/"):
                if len(link.split("/")) == 4:
                    print(link)
    except requests.RequestException as e:
        print(f"Error fetching page {page_url}: {e}")

# elements_with_data_th = soup.find_all(lambda tag: tag.has_attr('data-th'))

# Extract and print just the text from these elements
# names = []
# reviews = []
# type_of_wine = []
# varietal = []
# country = []
# region = []
# subregion = []
# producer = []
# product_category = []
# appelation = []
# cru = []
# vintage = []
# color = []
# format = []
# owc = []

# names.append(url.split("/")[-1].replace("-"," "))


# for element in elements_with_data_th:
#     data_th_value = element.get('data-th')
#     text = element.get_text(strip=True)  # strip=True removes any leading/trailing whitespace
#     if data_th_value == "Type of Wine":
#         type_of_wine.append(text)
#     elif data_th_value == "Varietal":
#         varietal.append(text)
#     elif data_th_value == "Country":
#         country.append(text)
#     elif data_th_value == "Region":
#         region.append(text)
#     elif data_th_value == "Subregion":
#         subregion.append(text)
#     elif data_th_value == "Appelation":
#         appelation.append(text)
#     elif "Cru" in data_th_value:
#         cru.append(text)
#     elif data_th_value == "Producer":
#         producer.append(text)
#     elif data_th_value == "Color":
#         color.append(text)
#     elif "Format" in data_th_value:
#         format.append(text)
#     elif data_th_value == "Vintage":
#         vintage.append(text)
#     elif "owc" in data_th_value:
#         owc.append(text)
#     elif data_th_value == "Product Category":
#         product_category.append(data_th_value)


# if len(type_of_wine) == 0:
#     type_of_wine.append(np.nan)
# if len(varietal) == 0:
#     varietal.append(np.nan)
# if len(country) == 0:
#     country.append(np.nan)
# if len(region) == 0:
#     region.append(np.nan)
# if len(subregion) == 0:
#     subregion.append(np.nan)
# if len(producer) == 0:
#     producer.append(np.nan)
# if len(product_category) == 0:
#     product_category.append(np.nan)
# if len(appelation) == 0:
#     appelation.append(np.nan)
# if len(cru) == 0:
#     cru.append(np.nan)
# if len(vintage) == 0:
#     vintage.append(np.nan)
# if len(color) == 0:
#     color.append(np.nan)
# if len(format) == 0:
#     format.append(np.nan)
# if len(owc) == 0:
#     owc.append(np.nan)



# reviews_li = []
# reviews = soup.find_all(class_="w-full text-base expand-attributes description")
# for review in reviews:
#     review_text = element.get_text(strip=True)
#     reviews_li.append(review_text)
    
# # Initialize a dictionary to store the scraped data
# wine_data = {
#     "Name" : names,
#     "Critic Reviews and Scores": reviews,
#     "Type of Wine": type_of_wine,
#     "Varietal": varietal,
#     "Country": country,
#     "Region": region,
#     "Subregion": subregion,
#     "Producer": producer,
#     "Product Category": product_category,
#     "Appellation": appelation,
#     "Cru": cru,
#     "Vintage": vintage,
#     "Color": color,
#     "Format (Size)": format,
#     "OWC": owc
# }

# # Example of extracting data (you'll need to locate the correct tags and classes)
# # This is a placeholder as each website's structure is unique
# # wine_data["Type of Wine"].append(soup.find(class_="wine-type-class").get_text())

# # Create a DataFrame from the dictionary
# df = pd.DataFrame(wine_data)

# # Export the DataFrame to an Excel file
# df.to_excel("wine_data.xlsx", index=False)
