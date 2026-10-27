#!/usr/bin/env python
# coding: utf-8

# In[6]:


import json
import requests
from bs4 import BeautifulSoup

def scrape_grocery_deals():
    # Example target: A public weekly ad or deal feed
    # (Replace with target store weekly ad URL or API endpoint)
    url = "https://drive.google.com/file/d/16A-c1i4zPG_OJEiveDWGvWnn73cHkyK1/view?pli=1"
    
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        scraped_deals = []
        
        # Example parsing logic (adjust based on the store's HTML structure)
        # Looking for product cards in the weekly ad
        product_cards = soup.find_all('div', class_='product-card')
        
        for card in product_cards:
            title = card.find('h3').text.strip() if card.find('h3') else "Special Item"
            price = card.find('span', class_='price').text.strip() if card.find('span', class_='price') else "$1.99"
            store = "Woodman's" # or dynamic based on page
            
            scraped_deals.append({
                "store": store,
                "item": title,
                "price": price,
                "category": "Produce & Groceries"
            })
            
        # Fallback sample data if site structure changes or blocks basic scraping
        if not scraped_deals:
            scraped_deals = [
                {"store": "Whole Foods", "item": "Organic Hass Avocados (4ct)", "price": "$3.99", "category": "Produce"},
                {"store": "Target", "item": "Good & Gather Organic Spinach", "price": "$2.49", "category": "Produce"}, {"store": "Woodman's", "item": "Organic Hass Avocados (4ct)"}
            ]

        # Save to deals.json which your website reads directly!
        with open('deals.json', 'w') as f:
            json.dump(scraped_deals, f, indent=4)
            
        print("Successfully updated deals.json!")

    except Exception as e:
        print(f"Scraping error: {e}")

if __name__ == "__main__":
    scrape_grocery_deals()


# In[7]:


get_ipython().system('pip install requests beautifulsoup4')


# In[8]:


def scrape_grocery_deals():
    # Example target: A public weekly ad or deal feed
    # (Replace with target store weekly ad URL or API endpoint)
    url = "https://www.wholefoodsmarket.com/sales-flyer?ref_=US_TRF_ALL_UFG_WFM_OTHER_1002390&store-id=10129"
    
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        scraped_deals = []
        
        # Example parsing logic (adjust based on the store's HTML structure)
        # Looking for product cards in the weekly ad
        product_cards = soup.find_all('div', class_='product-card')
        
        for card in product_cards:
            title = card.find('h3').text.strip() if card.find('h3') else "Special Item"
            price = card.find('span', class_='price').text.strip() if card.find('span', class_='price') else "$1.99"
            store = "Woodman's" # or dynamic based on page
            
            scraped_deals.append({
                "store": store,
                "item": title,
                "price": price,
                "category": "Produce & Groceries"
            })
            
        # Fallback sample data if site structure changes or blocks basic scraping
        if not scraped_deals:
            scraped_deals = [
                {"store": "Whole Foods", "item": "Organic Hass Avocados (4ct)", "price": "$3.99", "category": "Produce"},
                {"store": "Target", "item": "Good & Gather Organic Spinach", "price": "$2.49", "category": "Produce"}, {"store": "Woodman's", "item": "Organic Hass Avocados (4ct)"}
            ]

        # Save to deals.json which your website reads directly!
        with open('deals.json', 'w') as f:
            json.dump(scraped_deals, f, indent=4)
            
        print("Successfully updated deals.json!")

    except Exception as e:
        print(f"Scraping error: {e}")

if __name__ == "__main__":
    scrape_grocery_deals()


# In[9]:


def scrape_grocery_deals():
    # Example target: A public weekly ad or deal feed
    # (Replace with target store weekly ad URL or API endpoint)
    url = "https://www.wholefoodsmarket.com/sales-flyer?ref_=US_TRF_ALL_UFG_WFM_OTHER_1002390&store-id=10129"
    
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        scraped_deals = []
        
        # Example parsing logic (adjust based on the store's HTML structure)
        # Looking for product cards in the weekly ad
        product_cards = soup.find_all('div', class_='product-card')
        
        for card in product_cards:
            title = card.find('h3').text.strip() if card.find('h3') else "Special Item"
            price = card.find('span', class_='price').text.strip() if card.find('span', class_='price') else "$1.99"
            store = "Whole foods" # or dynamic based on page
            
            scraped_deals.append({
                "store": store,
                "item": title,
                "price": price,
                "category": "Produce & Groceries"
            })
            
        # Fallback sample data if site structure changes or blocks basic scraping
        if not scraped_deals:
            scraped_deals = [
                {"store": "Whole Foods", "item": "Organic Hass Avocados (4ct)", "price": "$3.99", "category": "Produce"},
                {"store": "Target", "item": "Good & Gather Organic Spinach", "price": "$2.49", "category": "Produce"}, {"store": "Woodman's", "item": "Organic Hass Avocados (4ct)"}
            ]

        # Save to deals.json which your website reads directly!
        with open('deals.json', 'w') as f:
            json.dump(scraped_deals, f, indent=4)
            
        print("Successfully updated deals.json!")

    except Exception as e:
        print(f"Scraping error: {e}")

if __name__ == "__main__":
    scrape_grocery_deals()


# In[10]:


def scrape_grocery_deals():
    # Example target: A public weekly ad or deal feed
    # (Replace with target store weekly ad URL or API endpoint)
    url = "https://www.target.com/c/top-deals/-/N-4xw74"
    
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        scraped_deals = []
        
        # Example parsing logic (adjust based on the store's HTML structure)
        # Looking for product cards in the weekly ad
        product_cards = soup.find_all('div', class_='product-card')
        
        for card in product_cards:
            title = card.find('h3').text.strip() if card.find('h3') else "Special Item"
            price = card.find('span', class_='price').text.strip() if card.find('span', class_='price') else "$1.99"
            store = "Target" # or dynamic based on page
            
            scraped_deals.append({
                "store": store,
                "item": title,
                "price": price,
                "category": "Produce & Groceries"
            })
            
        # Fallback sample data if site structure changes or blocks basic scraping
        if not scraped_deals:
            scraped_deals = [
                {"store": "Whole Foods", "item": "Organic Hass Avocados (4ct)", "price": "$3.99", "category": "Produce"},
                {"store": "Target", "item": "Good & Gather Organic Spinach", "price": "$2.49", "category": "Produce"}, {"store": "Woodman's", "item": "Organic Hass Avocados (4ct)"}
            ]

        # Save to deals.json which your website reads directly!
        with open('deals.json', 'w') as f:
            json.dump(scraped_deals, f, indent=4)
            
        print("Successfully updated deals.json!")

    except Exception as e:
        print(f"Scraping error: {e}")

if __name__ == "__main__":
    scrape_grocery_deals()


# In[11]:


def scrape_grocery_deals():
    # Example target: A public weekly ad or deal feed
    # (Replace with target store weekly ad URL or API endpoint)
    url = "https://www.jewelosco.com/weeklyad"
    
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        scraped_deals = []
        
        # Example parsing logic (adjust based on the store's HTML structure)
        # Looking for product cards in the weekly ad
        product_cards = soup.find_all('div', class_='product-card')
        
        for card in product_cards:
            title = card.find('h3').text.strip() if card.find('h3') else "Special Item"
            price = card.find('span', class_='price').text.strip() if card.find('span', class_='price') else "$1.99"
            store = "JewelOsco" # or dynamic based on page
            
            scraped_deals.append({
                "store": store,
                "item": title,
                "price": price,
                "category": "Produce & Groceries"
            })
            
        # Fallback sample data if site structure changes or blocks basic scraping
        if not scraped_deals:
            scraped_deals = [
                {"store": "Whole Foods", "item": "Organic Hass Avocados (4ct)", "price": "$3.99", "category": "Produce"},
                {"store": "Target", "item": "Good & Gather Organic Spinach", "price": "$2.49", "category": "Produce"}, {"store": "Woodman's", "item": "Organic Hass Avocados (4ct)"}
            ]

        # Save to deals.json which your website reads directly!
        with open('deals.json', 'w') as f:
            json.dump(scraped_deals, f, indent=4)
            
        print("Successfully updated deals.json!")

    except Exception as e:
        print(f"Scraping error: {e}")

if __name__ == "__main__":
    scrape_grocery_deals()


# In[12]:


def scrape_grocery_deals():
    # Example target: A public weekly ad or deal feed
    # (Replace with target store weekly ad URL or API endpoint)
    url = "https://www.patelbros.com/store-promotions"
    
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        scraped_deals = []
        
        # Example parsing logic (adjust based on the store's HTML structure)
        # Looking for product cards in the weekly ad
        product_cards = soup.find_all('div', class_='product-card')
        
        for card in product_cards:
            title = card.find('h3').text.strip() if card.find('h3') else "Special Item"
            price = card.find('span', class_='price').text.strip() if card.find('span', class_='price') else "$1.99"
            store = "Patel Brothers" # or dynamic based on page
            
            scraped_deals.append({
                "store": store,
                "item": title,
                "price": price,
                "category": "Produce & Groceries"
            })
            
        # Fallback sample data if site structure changes or blocks basic scraping
        if not scraped_deals:
            scraped_deals = [
                {"store": "Whole Foods", "item": "Organic Hass Avocados (4ct)", "price": "$3.99", "category": "Produce"},
                {"store": "Target", "item": "Good & Gather Organic Spinach", "price": "$2.49", "category": "Produce"}, {"store": "Woodman's", "item": "Organic Hass Avocados (4ct)"}
            ]

        # Save to deals.json which your website reads directly!
        with open('deals.json', 'w') as f:
            json.dump(scraped_deals, f, indent=4)
            
        print("Successfully updated deals.json!")

    except Exception as e:
        print(f"Scraping error: {e}")

if __name__ == "__main__":
    scrape_grocery_deals()


# In[ ]:




