from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import json


options = webdriver.ChromeOptions()
options.add_argument('--headless')  # runs browser in background
options.add_argument('--disable-gpu')  # for Windows
options.add_argument('--window-size=1920x1080')  # optional but recommended

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

url = "https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart"
driver.get(url)


results_list = driver.find_elements(By.CSS_SELECTOR, 'li.row.cp-search-result-item')
print(f"Found {len(results_list)} results on this page")


results = []

for item in results_list:
    # Title
    title_elem = item.find_element(By.CSS_SELECTOR, 'span.title-content')
    title = title_elem.text.strip()
    
    # Authors (may be multiple)
    author_elems = item.find_elements(By.CSS_SELECTOR, 'a.author-link')
    authors = "; ".join([a.text.strip() for a in author_elems])
    
    # Format + Year
    format_elem = item.find_element(By.CSS_SELECTOR, 'span.cp-screen-reader-message')
    format_year = format_elem.text.strip()
    
    # Add to results list
    results.append({
        "Title": title,
        "Author": authors,
        "Format-Year": format_year
    })

df = pd.DataFrame(results)
print(df)

# Save to CSV
df.to_csv("get_books.csv", index=False)

# Save to JSON
with open("get_books.json", "w") as f:
    json.dump(results, f, indent=4)

driver.quit()
