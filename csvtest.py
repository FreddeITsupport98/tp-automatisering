import csv
with open('users.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        #print(row)
        print(row['firstname'], row['lastname'], row['email'])

with open('users.csv', 'w', newline='') as csvfile:
    fieldnames = ['firstname', 'lastname', 'email']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    firstname = input("Förnamn: ")
    lastname = input("Efternamn: ")
    email = input("Email: ")

    writer.writeheader()
    writer.writerow({'firstname': firstname, 'lastname': lastname, 'email': email})