import requests
from trust_algorithm import trust_alg, update_blacklist

# urls of site
base_url = "https://dsc180-decentralized-location.herokuapp.com/locationConsensus/" # herokuapp url
# base_url = "http://127.0.0.1:8000/locationConsensus/" # local test url
interaction_url = base_url + "interactions/"

# gets interaction data
data = requests.get(interaction_url).json()

flagged_users = trust_alg(data)
update_blacklist(flagged_users)

print("Trust algorithm ran successfully")