
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import time

# Set up Chrome driver
driver = webdriver.Chrome()

# Open OWASP Top 10 page
driver.get("https://owasp.org/www-project-top-ten/")

# Wait until the Top 10 list is visible
top10_ul = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//ul[li/a/strong]"))
)

# Find all list items under this <ul>
top10_items = top10_ul.find_elements(By.TAG_NAME, "li")

top10_data = []

for item in top10_items:
    try:
        a_tag = item.find_element(By.TAG_NAME, "a")
        strong_tag = a_tag.find_element(By.TAG_NAME, "strong")
        title = strong_tag.text.strip()
        link = a_tag.get_attribute("href").strip()
        top10_data.append({"title": title, "link": link})
    except:
        # skip any items that don't match structure
        continue

# Print the list to verify
print(top10_data)

# Save to CSV
csv_file = "owasp_top_10.csv"
with open(csv_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["title", "link"])
    writer.writeheader()
    writer.writerows(top10_data)

print(f"✅ Saved OWASP Top 10 to {csv_file}")

# Keep browser open for 10 seconds (for debugging)
time.sleep(10)

# Close the driver
driver.quit()


