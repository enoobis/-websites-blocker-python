import time
from datetime import datetime as dt

# list of websites to block
websites_to_block = ["www.facebook.com", "www.twitter.com" , "www.instagram.com" , "www.tiktok.com"]

# host file location (for Windows it is C:\Windows\System32\drivers\etc\hosts)
hosts_file = "C:\Windows\System32\drivers\etc\hosts"

# url to redirect blocked websites to
redirect_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

# loop to check the current time
while True:
    # block websites all day
    with open(hosts_file, 'r+') as file:
        content = file.read()
        for website in websites_to_block:
            if website in content:
                pass
            else:
                # block website by redirecting to a specific URL (in this case a Rickroll video)
                file.write("\n127.0.0.1 " + website)
                file.write("\n127.0.0.1 " + redirect_url)
    time.sleep(5)