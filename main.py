import argparse
from social_media import check_username, PLATFORMS

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--username", help="Username to search on supported platforms")
    args = parser.parse_args()

    if args.username:
        username = args.username
        print(f"\nSearching for username: {username}\n")

        for platform in PLATFORMS:
            found = check_username(platform, username)
            url = PLATFORMS[platform].format(username=username)

            if found:
                print(f"Found on {platform:<10} {url}")
            else:
                print(f"Not found on {platform}")

    else:
        print("⚠️ Use --username to search (e.g., python main.py --username johndoe)")

if __name__ == "__main__":
    main()
