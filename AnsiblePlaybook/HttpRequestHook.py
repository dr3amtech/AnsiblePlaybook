import requests


try:
	url = "http://joshuajoseph7:113f2657f84fc5ca88f7004e9cd155766f@localhost:8080/job/FirstPipline/build?token=JENKINSBUILDFREE"
	req = requests.get(url)
except requests.exceptions.RequestException as e:  # This is the correct syntax
    print e
    sys.exit(1)
