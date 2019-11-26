import csv
with open('users.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        #print(row)
        print(row['firstname'], row['lastname'], row['email'])

with open('users.csv', 'w', newline='') as csvfile:
    fieldnames = ['firstname', 'lastname', 'email']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'firstname': 'Baked', 'lastname': 'Beans', 'email': 'a@b'})
    writer.writerow({'firstname': 'Lovely', 'lastname': 'Spam', 'email': 'asdf@b'})
    writer.writerow({'firstname': 'Wonderful', 'lastname': 'Spam', 'email': 'awefwef@b'})