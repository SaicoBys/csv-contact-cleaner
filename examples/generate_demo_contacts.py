from faker import Faker
import csv
import os

fake = Faker()
num_contacts = 50

# Asegura que el directorio data existe
os.makedirs('../data', exist_ok=True)

output_path = '../data/demo_contacts.csv'

with open(output_path, 'w', newline='') as csvfile:
    fieldnames = ['Name', 'Email', 'Phone', 'Company', 'Position']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for _ in range(num_contacts):
        writer.writerow({
            'Name': fake.name(),
            'Email': fake.email(),
            'Phone': fake.phone_number(),
            'Company': fake.company(),
            'Position': fake.job()
        })

print(f"Demo contacts generated in {output_path}") 