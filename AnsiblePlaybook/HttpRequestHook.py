#! /usr/local/bin/python
import requests


try:
	url = "http://joshuajoseph7:$JENKINS_TOKEN@localhost:8080/job/FirstPipeline//buildWithParameters?token=JENKINSBUILDFREE"
	req = requests.get(url)
except requests.exceptions.RequestException as e:  # This is the correct syntax
    print e
    sys.exit(1)