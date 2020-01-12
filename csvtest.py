import csv

with open('users2.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        #print(row)
        print(row['first_name'], row['last_name'], row['email'], row['gender'], row['OU'], row['DC'], row['DC'])

with open('users.csv', 'w', newline='') as csvfile:
    fieldnames = ['first_name', 'last_name', 'email', 'gender', 'OU', 'DC', 'DC']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    first_name = input("Förnamn: ")
    last_name = input("Efternamn: ")
    email = input("Email: ")
    gender = input("Din kön som: Male eller Female: ")
    OU = input("OU (organations unit): ")
    DC = input("DC (Servernamn): ")
    DC = input("DC (.com eller.se?): ")
     

    writer.writeheader()
    writer.writerow({'first_name': first_name, 'last_name': last_name, 'email': email, 'gender': gender, 'OU=': OU, 'DC=': DC, 'DC=': DC})
print(csv)