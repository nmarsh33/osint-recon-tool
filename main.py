import argparse
import requests
 
def check_github(username):
	url = f"https://github.com/{username}"
	try:
	   response = requests.get(url, timeout=5)
	   return response.status_code == 200
	except requests.RequestException:
	   return False
 
def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("--username", help="Username to search on Github")
	args = parser.parse_args()
 
	if args.username:
		found = check_github(args.username)
		if found:
			print(f"Username '{args.username}' found on Github.")
		else:
			print(f"Username '{args.username}' not found on Github.")
	else:
		print("Use --username to search for Github user.")
 
 
 
main()