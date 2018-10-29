import requests


try:
	url = "http://joshuajoseph7:<userT>@localhost:8080/job/Humanoid_Playground/build?token=JENKINSBUILDFREE"
	req = requests.get(url)
except requests.exceptions.RequestException as e:  # This is the correct syntax
    print e
    sys.exit(1)
