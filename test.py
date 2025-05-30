import requests

url = "https://www.instagram.com"  # Replace with the URL you want to fetch
response = requests.get(url)
html_content = response.text
print(html_content)