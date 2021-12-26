# Backgound information source:
# https://towardsdatascience.com/scraping-news-and-articles-from-public-apis-with-python-be84521d85b9

import requests
from pprint import pprint
import os
from config_folder import config
import json
import pandas as pd
desired_width = 320
pd.set_option('display.width', desired_width)
import functions_file

nyt_apikey = os.getenv('NYTIMES_APIKEY', config.nyt_api_key)


# Top Stories:
# https://developer.nytimes.com/docs/top-stories-product/1/overview
section = "world"
query_url = f"https://api.nytimes.com/svc/topstories/v2/{section}.json?api-key={nyt_apikey}"

r = requests.get(query_url)             # Requesting data
# r.json()
# pprint(r.json())
json_data = json.dumps(r.json())
data_file = open("test.json","w")
data_file.write(json_data)
data_file.close()

# df = pd.read_json("test.json")          # Read in the json file created above
# print(df.head())
# pd.json_normalize("test.json", record_path=["results"], meta=['title','url'])

with open('test.json') as f:
    nyt_data = json.load(f)

# print(nyt_data['results'][0]['byline'])

# print(nyt_data.keys())                      # Lets me see the keys to understand where the data is
nyt_data_results = nyt_data['results']      # Gathers only the data that comes in under "results"
df = pd.DataFrame(nyt_data_results)         # Converts results to a DF

# Adding in work for accessing The Guardian
# guardian_query = "science"
# Below is searching Sections
# guardian_query_url = f"https://content.guardianapis.com/sections?" \
#             f"api-key={config.guardian_api_key}" \

# Below is searching Tags
# guardian_query = "weather"
# section = "news"
# page = "1"
# guardian_query_url = f"http://content.guardianapis.com/tags?" \
#             f"api-key={config.guardian_api_key}" \
#             f"&q={guardian_query}" \
#             f"&page={page}"

query = "(hurricane OR storm)"
query_fields = "body"
section = "news"  # https://open-platform.theguardian.com/documentation/section
tag = "world/extreme-weather"  # https://open-platform.theguardian.com/documentation/tag
from_date = "2019-01-01"
guardian_query_url = f"https://content.guardianapis.com/search?" \
            f"api-key={config.guardian_api_key}" \
            f"&q={query}" \
            f"&query-fields={query_fields}" \
            f"&section={section}" \
            f"&tag={tag}" \
            f"&from-date={from_date}" \
            f"&show-fields=headline,byline,starRating,shortUrl"

r_guardian = requests.get(guardian_query_url)
# pprint(r_guardian.json())
guardian_result = json.dumps(r_guardian.json())
print(guardian_result)

guardian_datafile = open("guardian_datafile.json","w")
guardian_datafile.write(guardian_result)
guardian_datafile.close()

with open('guardian_datafile.json') as f:
    guardian_data = json.load(f)

guardian_results = guardian_data['response']
guardian_results = guardian_results["results"]
guardian_df = pd.DataFrame(guardian_results)
guardian_df.head(10)

# print(df.head())

# print(nyt_data_results[0])
num = 1
nyt_titles = []
message = """
<!DOCTYPE html>
<html>
<body>
<h1>This is a heading</h1>
</body>
</html>
"""
nyt_titles.append(message)
for i in range(len(nyt_data_results)):
    # print(nyt_data_results[i]['title'])
    # nyt_titles.append("<h1>")
    # nyt_titles.append("<title>New York Times Top Stories</title>")
    nyt_titles.append(str(num) + ":")
    nyt_titles.append(nyt_data_results[i]['title'])
    nyt_titles.append(nyt_data_results[i]['url'])
    nyt_titles.append("<br>")
    num += 1

nyt_titles_df = pd.DataFrame([nyt_titles])
nyt_titles_df = nyt_titles_df.T

# nyt_titles_df.to_csv("titles_file.txt", sep='\t', encoding='utf-8')
nyt_titles_df.to_csv("titles_file.html", index=False, sep='\t', encoding='utf-8')
# nyt_titles_df.reset_index(drop=True, inplace=True)
# nyt_titles.to_csv("titles_file.html", sep='\t', encoding='utf-8')
# print(nyt_data.keys())

## Now to send my file as an attachment in an email
# Request all access (permission to read/send/receive emails, manage the inbox, and more)
# SCOPES = ['https://mail.google.com/']

# get the Gmail API service
service = functions_file.gmail_authenticate()

file_to_send ="titles_file.html"

functions_file.send_message(service, config.sending_email, "This is a subject", "This is the body of the email", [file_to_send])

