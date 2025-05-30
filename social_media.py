import requests
import re

PLATFORMS = {
    "instagram": "https://www.instagram.com/{username}/",
    "github": "https://github.com/{username}",
    "reddit": "https://www.reddit.com/user/{username}/",
    "twitter": "https://x.com/{username}",
}

def instagram_exists(username):
    url = f"https://www.instagram.com/{username}/"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(url, headers=headers, timeout=5)

        if response.status_code != 200:
            return False

        if "Sorry, this page isn't available." in response.text:
            return False

        if re.search(rf"<title>.*\(@{username.lower()}\)", response.text, re.IGNORECASE):
            return True
        if '"biography":"' in response.text or '"edge_owner_to_timeline_media":' in response.text:
            return True

        return False

    except requests.RequestException:
        return False

def check_username(platform, username):
    if platform.lower() not in PLATFORMS:
        raise ValueError(f"Platform '{platform}' is not supported.")

    url = PLATFORMS[platform.lower()].format(username=username)
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(url, headers=headers, timeout=5)

        if platform.lower() == "instagram":
            return instagram_exists(username)

        elif platform.lower() == "reddit":
            return response.status_code == 200 and "Sorry, nobody on Reddit goes by that name" not in response.text

        return response.status_code == 200

    except requests.RequestException:
        return False
