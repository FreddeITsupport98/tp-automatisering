import datetime

firstname = "Jens"
lastname = "Andreasson"
now = datetime.datetime.now()
year = now.year

# umu old username policy
username = firstname[0] + firstname[-2:]+ lastname[0:2] + lastname[-1:] + str(year)[-2:]

print(username.lower())