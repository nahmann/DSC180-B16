import json
import requests
from datetime import datetime, timezone, timedelta
import pandas as pd

# urls of site
# base_url = "https://dsc180-decentralized-location.herokuapp.com/locationConsensus/"
base_url = "https://http://127.0.0.1:8000//locationConsensus/" # local test url
interaction_url = base_url + "interactions/"
blacklist_url = base_url + "blacklist/"


def update_blacklist(users, url = None):
    """
    Updates blacklist with new flagged users

    users: list of users to update blacklist
    url: url of blacklist to update. Uses the site blacklist url by default
    """
    if url is None:
        url = blacklist_url

    print(users)

    for user in users:
        toSend  = {'userID': user}
        requests.post(url, data = toSend)

def trust_alg(data, time = None, hours = None):
    """
    Runs trust algorithm on data passed in. Current trust algorithm is based 
    off of a majority trust model. It will return a list of untrustworthy users. 
    By default, the method will run the algorithm on data within the past hour.

    data: Expects json data retrieved from requests. Expects time, from_user,
    and spotted_users as columns in the data
    time: A datetime object of what date and time to use to filter data. By default 
    the method will use the current date and time in utc timezone.
    hours: number of hours to use to make a timeframe of valid data. Hours will 
    be subtracted from the time parameter to make the timeframe. By default the 
    method will consider only the past hour.
    """

    if time is None:
        time = datetime.now(timezone.utc)

    if hours is None:
        hours = 1

    cutoff = 0.5 # cutoff percentage to be marked for blacklist
    time = time.astimezone(timezone.utc) # converts datetime to utc time incate date is a passed parameter
    past_timeframe = time - timedelta(hours)

    try:
        df = pd.DataFrame(data)

        print(df.columns)
        # filter data to only include interactions within the past timeframe. Default is past hour
        df["time"] = pd.to_datetime(df["time"])
        df = df.loc[df["time"] > past_timeframe]
    except KeyError:
        print("no time data")
        exit()
        

    # cleaning spotted_users so that it becomes a list
    df["spotted_users"] = df["spotted_users"].str[1:-1].str.split(", ")

    # turning every name in spotted user into rows
    df = df.explode("spotted_users")

    # count number of times a user was spotted / number of users
    # trust algorithm: if a majority of people around you do not agree with your location then you are untrustworthy
    spotted_percentage = df.groupby("spotted_users")["from_user"].count() / df["from_user"].nunique()
    flagged_users = spotted_percentage[spotted_percentage > cutoff]
    return flagged_users.index.tolist()
