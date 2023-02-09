import requests
from datetime import datetime, timezone, timedelta
import pandas as pd

# urls of site
base_url = "https://dsc180-decentralized-location.herokuapp.com/locationConsensus/"
interaction_url = base_url + "interactions/"
blacklist_url = base_url + "blacklist/"

# fields
cuttoff = 0.5 # cutoff percentage to be marked for blacklist
now = datetime.now(timezone.utc)
past_hour = now - timedelta(hours=1) # script is run hourly

def update_blacklist(users):
    """
    Updates blacklist with new flagged users
    """
    for user in users:
        toSend  = {'userID': user}
        requests.post(blacklist_url, data = toSend)

try:
    # gets interaction data
    data = requests.get(interaction_url).json()
    df = pd.DataFrame(data)

    # filter data to only include interactions within the past hour
    df["time"] = pd.to_datetime(df["time"])
    past_hour_df = df.loc[df["time"] > past_hour]
except KeyError:
    print("no time data")
    exit()

# count number of times a user was spotted / number of users
# trust algorithm: if a majority of the people say you were spotted, then 
# you are untrustworthy
spotted_percentage = past_hour_df.groupby("spotted_users")["from_user"].count() / past_hour_df["from_user"].nunique()
flagged_users = spotted_percentage[spotted_percentage > cuttoff]

update_blacklist(flagged_users.index)

print("Trust algorithm ran successfully")