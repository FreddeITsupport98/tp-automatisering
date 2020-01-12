import csv

with open('users2.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        #print(row)
        print(row['first_name'], row['last_name'], row['email'], row['gender'], row['OU='], row['DC1='], row['DC2='])

with open('users2.csv', 'w', newline='') as csvfile:
    fieldnames = ['first_name', 'last_name', 'email', 'gender', 'OU=', 'DC1=', 'DC2=']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    first_name = input("Förnamn: ")
    last_name = input("Efternamn: ")
    email = input("Email: ")
    gender = input("Din kön som: Male eller Female: ")
    OU = input("OU= (organations unit): ")
    DC1 = input("DC= (Servernamn): ")
    DC2 = input("DC= (.com eller.se?): ")
     

    writer.writeheader()
    writer.writerow({'first_name': first_name, 'last_name': last_name, 'email': email, 'gender': gender, 'OU=': OU, 'DC1=': DC1, 'DC2=': DC2})