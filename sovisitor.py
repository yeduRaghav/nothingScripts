import requests
from bs4 import BeautifulSoup

try:
    response = requests.get("https://stackoverflow.com/users/login?ssrc=head")
    print(response.content)
    
except requests.connectionError:
    print("connectionError")

# soResponse = urlopen("https://stackoverflow.com/users/4127441/rgv")
# soResponse
# bsInstance = BeautifulSoup(soResponse.read(), "html.parser")
# print(bsInstance)
