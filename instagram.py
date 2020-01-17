import sys
import requests
username = sys.argv[1]
print(f'[+] Getting {username} info ...')
endpoint = f"https://www.instagram.com/{username}/?__a=1"
user_info = requests.get(endpoint).json()
user_profile_pic_url = user_info ['graphql']['user'] ['profile_pic_url_hd']
# Download Profile
print(f'[+] Downloading {username} Profile Picture ...')
user_profile_pic_content = requests.get(user_profile_pic_url).content
with open(f'{username}.jpg','wb') as pic_file:
    pic_file.write(user_profile_pic_content)
print(f'[+] {username} Profile Picture Downloaded Successfully.')