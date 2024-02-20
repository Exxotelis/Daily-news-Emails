
import requests
from send_email import send_email

topic = "tesla"
api_key = "890603a55bfa47048e4490069ebee18c"
url = f"https://newsapi.org/v2/everything?q={topic}&" \
    "sortBy=publishedAt&apiKey=" \
    "890603a55bfa47048e4490069ebee18c&languge=en"

# Make request
response = requests.get(url)
# Get a dictionary with data
content = response.json()

# Access the article titles and description
body = ""
for article in content["articles"][:20]:
    if article["title"] is not None:
        body = body + article["title"] + "\n"\
            + article["url"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)
