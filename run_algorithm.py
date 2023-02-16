import requests
from trust_algorithm import trust_alg, update_blacklist

# urls of site
base_url = "https://dsc180-decentralized-location.herokuapp.com/locationConsensus/"
interaction_url = base_url + "interactions/"

# gets interaction data
data = requests.get(interaction_url).json()

flagged_users = trust_alg(data)
update_blacklist(flagged_users.index)

print("Trust algorithm ran successfully")