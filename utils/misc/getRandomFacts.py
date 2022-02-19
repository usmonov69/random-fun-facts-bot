

import requests

url = "https://random-facts2.p.rapidapi.com/getfact"
def getFacts():
	headers = {
	    'x-rapidapi-host': "random-facts2.p.rapidapi.com",
	    'x-rapidapi-key': "9c33c1c667msh7b56fe811d2de8dp1b2e49jsnee196e80ca61"
	    }

	response = requests.request("GET", url, headers=headers)
	res = response.json()
	# print(res)
	allFact = res['Fact']
	return allFact

if __name__ == "__main__":
	from pprint import pprint as print
	print(getFacts())
