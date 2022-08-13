#first option imports
from quote import quote
import random
#second option imports
import requests

#first option code
print(“Enter the name of your favorite author/person?”)

# take the name of the author/person from the user
q_author = input()

# store the quotes of that particular author in quotes variable
quotes = quote(q_author)

# use random function to retrieve any random quote i.e inside quotes variable
quote_no = random.randint(1, len(quotes))

# finally will display the quote along with the name of the author as output
print(“Author: “, quotes[quote_no][‘author’])
print(“ →”, quotes[quote_no][‘quote’])

#second option code
## function that gets the random quote
def get_random_quote():
	try:
		## making the get request
		response = requests.get("https://quote-garden.herokuapp.com/api/v3/quotes/random")
		if response.status_code == 200:
			## extracting the core data
			json_data = response.json()
			data = json_data['data']

			## getting the quote from the data
			print(data[0]['quoteText'])
		else:
			print("Error while getting quote")
	except:
		print("Something went wrong! Try Again!")


get_random_quote()



