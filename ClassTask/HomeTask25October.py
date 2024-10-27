#HomeTask of 25 OCtober
#Python Automation Web Scrapping Script For Collecting Atleast 100 Shopify Website Link
#Done By Md Sanjid Alvi
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import openpyxl


driver = webdriver.Chrome()


search_term = 'site:myshopify.com'


target_links = 500


driver.get('https://www.google.com')
search_box = driver.find_element(By.NAME, 'q')
search_box.send_keys(search_term)
search_box.send_keys(Keys.RETURN)

time.sleep(2)  


shopify_links = set()


def extract_links():
    results = driver.find_elements(By.XPATH, '//a')
    for result in results:
        link = result.get_attribute('href')
      
        if link and "myshopify.com" in link and "google.com" not in link:
            shopify_links.add(link)


while len(shopify_links) < target_links:
    extract_links()
    
    
    try:
        next_button = driver.find_element(By.XPATH, "//a[@id='pnnext']")
        next_button.click()
        time.sleep(2)  
    except:
        print("No more pages available or blocked by Google.")
        break


driver.quit()


workbook = openpyxl.Workbook()
sheet = workbook.active
sheet.title = "Shopify Links"


sheet['A1'] = 'Shopify Websites'


for i, link in enumerate(shopify_links, start=2):
    sheet[f'A{i}'] = link


workbook.save("shopify_websites.xlsx")

print(f"Collected by Md Sanjid Alvi {len(shopify_links)} Shopify links and saved to shopify_websites.xlsx")
