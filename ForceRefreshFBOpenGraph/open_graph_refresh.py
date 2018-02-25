"""
@company: Pericror
Description:
    Demo code for https://www.pericror.com/software/programatically-force-update-facebook-open-graph/
"""

import requests
import time

api_url = "https://graph.facebook.com"
access_token = "paste your long live access token here"
graph_url = "paste the link of the page you want to refresh here"
post_data = { 'id':graph_url, 'scrape':True, 'access_token':access_token }
# Beware of rate limiting if trying to increase frequency.
refresh_rate = 30 # refresh rate in second

while True:
    try:
        resp = requests.post(api_url, data = post_data)
        if resp.status_code == 200:
            contents = resp.json()
            print(contents['title'])
        else:
            error = "Warning: Status Code {}\n{}\n".format(
                resp.status_code, resp.content)
            print(error)
            raise RuntimeWarning(error)
    except Exception as e:
        f = open ("open_graph_refresher.log", "a")
        f.write("{} : {}".format(type(e), e))
        f.close()
        print(e)
    time.sleep(refresh_rate)