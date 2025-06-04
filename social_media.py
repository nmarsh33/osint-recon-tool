import requests

PLATFORMS = {
    "github": "https://github.com/{username}",
    "reddit": "https://www.reddit.com/user/{username}/",
    "youtube": "https://youtube.com/@{username}",
    "stackoverflow": "https://api.stackexchange.com/2.3/users/{username}?site=stackoverflow",
}

def check_username(platform, username):
    if platform.lower() not in PLATFORMS:
        raise ValueError(f"Platform '{platform}' is not supported.")

    url = PLATFORMS[platform.lower()].format(username=username)
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    try:
        response = requests.get(url, headers=headers, timeout=5)

        if platform.lower() == "reddit":
            return response.status_code == 200 and "Sorry, nobody on Reddit goes by that name" not in response.text

        return response.status_code == 200

    except requests.RequestException:
        return False