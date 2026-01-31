import csv
import random

def generate_capped_contracts(filename, num_rows):
    divisions = ["North America", "EMEA", "APAC", "LATAM", "Public Sector"]
    products = ["SaaS Basic", "Support Tier 1", "API Call Bundle", "50GB Plan", "Firewall Lite"]
    customers = ["Alpha Corp", "Beta Ltd", "Gamma Sys", "Delta S.A.", "Epsilon Inc", "Zeta Group"]
    suffixes = ["Monthly", "Standard", "Basic", "Add-on", "Entry-Level"]
    sales_reps = ["Daniel", "Heath", "Parker", "Arthur", "Shiva", "Vashon", "Rijo", "Madhu", "Connor", "Abi", "Niket", "Steve"]

    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Writing the header
        writer.writerow(["Division", "ContractNo", "ContractName", "Customer","Sales_Rep", "Product", "Price"])

        for i in range(1, num_rows + 1):
            div = random.choice(divisions)
            c_no = f"CN-{random.randint(1000, 9999)}"
            prod = random.choice(products)
            c_name = f"{prod} {random.choice(suffixes)}"
            cust = random.choice(customers)
            rep = random.choice(sales_reps)
            
            # Generate price between 5.00 and 100.00
            price = round(random.uniform(5.00, 100.00), 2)

            writer.writerow([div, c_no, c_name, cust, rep, prod, f"${price:.2f}"])

generate_capped_contracts('contracts.csv', 10000)
print("Success! 'contracts_capped_10k.csv' created with 10,000 rows.")