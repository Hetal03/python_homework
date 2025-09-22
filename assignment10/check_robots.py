# Task 1: Review robots.txt to Ensure Policy Compliance
# This script fetches robots.txt from Durham County Library and shows the rules.

import requests

# URL for robots.txt
url = "https://durhamcountylibrary.org/robots.txt"

# Use a polite User-Agent (so site owners know who is making the request)
headers = {
    "User-Agent": "Assignment10Bot/1.0 (contact: your_email@example.com)"
}

def main():
    print("Fetching robots.txt from Durham County Library...")

    # Make a request to get robots.txt
    response = requests.get(url, headers=headers)

    # Check if we got the file
    if response.status_code == 200:
        print("\nrobots.txt successfully fetched!\n")
        text = response.text

        # Save a local copy so you can submit it with your assignment
        with open("robots.txt", "w", encoding="utf-8") as f:
            f.write(text)

        print("First 30 lines of robots.txt:\n")
        for i, line in enumerate(text.splitlines()[:30], start=1):
            print(f"{i:02d}: {line}")

    else:
        print(f"Could not fetch robots.txt. Status code: {response.status_code}")

if __name__ == "__main__":
    main()
