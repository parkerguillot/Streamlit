import sqlite3
import pandas as pd



#code used to generate orignal set of data
# # Initialize Faker for realistic names
# fake = Faker()

# def generate_contracts(n=10000):
#     data = []
    
#     # Using a set to ensure absolute uniqueness for Contract No
#     used_contract_nos = set()
    
#     divisions = ['West', 'East', 'SouthWest', 'NorthEast', 'Central']
#     products = ['ABC Stone', '#57 Stone', '#4 Stone', '#67 Stone', 'Rip Rap', 'Surge Stone', 'Railroad Ballast', 'Screenings', 'Pea Gravel', 'Mason Sand', 'Concrete Sand']
#     sales_reps = ["Daniel", "Heath", "Parker", "Arthur", "Shiva", "Vashon", "Rijo", "Madhu", "Connor", "Abi", "Niket", "Steve"]

#     while len(data) < n:
#         # Generate a unique Contract No (e.g., CNT-12345678)
#         c_no = f"CNT-{''.join(random.choices(string.digits, k=8))}"
        
#         if c_no not in used_contract_nos:
#             used_contract_nos.add(c_no)
            
#             record = {
#                 "index": len(data),
#                 "contract_no": c_no,
#                 "division": random.choice(divisions),
#                 "product_name": random.choice(products),
#                 "customer": fake.company(),
#                 "sales_rep": random.choice(sales_reps),
#                 "price": round(random.uniform(10.00, 50.00), 2)
#             }
#             data.append(record)

#     return pd.DataFrame(data)

# # Execute
# df = generate_contracts(10000)

# # Preview the first few rows
# print(df.head())

# # Optional: Save to CSV
# df.to_csv("contracts_data.csv", index=False)






df = pd.read_csv('contracts_data.csv')

conn = sqlite3.connect('streamlit.db')

df.to_sql('CONTRACTS', conn, if_exists='append')

c = conn.cursor()

conn.commit()

conn.close()






# # Division,ContractNo,ContractName,Customer,Sales_Rep,Product,Price
# c.execute("""CREATE TABLE CONTRACTS (
#           ID integer PRIMARY KEY,
#           DIVISION text not null,
#           CONTRACT_NO text not null,
#           CUSTOMER text not null,
#           SALES_REP text not null,
#           PRODUCT text not null,
#           Price decimal not null
#           )
# """)

