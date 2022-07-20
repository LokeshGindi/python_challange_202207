"""
Author: Lokesh G
Usage:  python fetch_sport_api_data.py --event_type "event1" "event2" --locale LC_ALL="en_GB"
Example:
      python fetch_sport_api_data.py --event_type "f1Results" "Tennis"
"""
from  requests import request,exceptions
from json import loads
from locale import setlocale, getlocale, LC_ALL
import argparse

# Handle the args here
parser = argparse.ArgumentParser(description='Fetch Sport Results Program.')
parser.add_argument('--event_type',
                        type=str,
                        nargs='*',
                        default=['f1Results'],
                        help='Type of sports event')
parser.add_argument('--locale_conf', nargs='*')
args = parser.parse_args()

# Parse the locale key value args here
parsed_conf = {}
if args.locale_conf:
    for pair in args.locale_conf:
        print("pair", pair)
        key, value = pair.split('=')
        parsed_conf[key] = value

#Fetch the default locale
loc = getlocale()
print("Default locale:", loc)
#Set locale properties
#Ex: locale.setlocale(locale.LC_ALL, 'en_GB')
if args.locale_conf:
    for locale_key,locale_value in parsed_conf.items():
        setlocale(LC_ALL, locale_value)

#MAIN Program begins here
# TODO: Keep the below params in separate param file and import the file here for better control
headers = {
    'Content-Type': "application/json",
    'cache-control': "no-cache"
    }
url = "https://ancient-wood-1161.getsandbox.com:443/results"
try:
    response = request("POST", url,headers=headers)
    data= response.text
    parse_json = loads(data)
    print(parse_json)
except exceptions.Timeout:
    # Maybe set up for a retry, or continue in a retry loop
    print("Retry attempt..")
except exceptions.TooManyRedirects:
    # Tell the user their URL was bad and try a different one
    print("Bad URL..")
except exceptions.RequestException as e:
    # catastrophic error. bail.
    raise SystemExit(e)

#List of Input sports events
event_names_list = parse_json.keys()
print("Sports Event list", event_names_list)

# Parse the sports events
for event_name,event_data in parse_json.items():
    # Validate the given event name here
    if event_name in args.event_type:
        print("event_name:",event_name)
        df = pd.DataFrame(event_data)
        # Reverse the sports results in chronological order
        df["publicationDate"] = pd.to_datetime(df["publicationDate"], format="%b %d, %Y %X %p")
        df.sort_values(by='publicationDate', ascending=False, inplace=True)
        # df.info(verbose=True)
        print(df)

# restore saved locale
if not args.locale_conf:
    setlocale(LC_ALL, loc)