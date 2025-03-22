#Dict working and .get() method explained 

a = {
    "name":"aditya",
    "language" : "python",
    "joke" : "Why are you gay?"
    }

print(a.get("name", "Oops! Couldn't get that"))
#As "name" key exists in this dict, the "Oops! Couldn't get that" isnt printed

print(a.get("punchline", "Oops! Couldn't get that"))
#As there's no key named "punchline" in the dictionary therefore "Oops! Couldn't get that" is printed
#This same dict mechanism is used by request and jokeAPI while fetching a joke in Jokingo 3.0