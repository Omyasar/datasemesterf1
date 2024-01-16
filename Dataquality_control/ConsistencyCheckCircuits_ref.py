import psycopg2

# Connect PostgreSQL database
conn = psycopg2.connect(
        host="localhost",
        port=5433,
        user="postgres",
        password="Kwvfiw727:",
        database="f1database"
)

# Create a cursor object
cursor = conn.cursor()

# Execute SELECT query to fetch the URLs from specified table
cursor.execute("SELECT circuit_ref, name FROM circuits")

# Fetch all rows and extract the URLs
rows = cursor.fetchall()
circuit_ref_list = [row[0] for row in rows]
circuit_name_list = [row[1] for row in rows]

# Close the cursor and connection
cursor.close()
conn.close()

# Print the list to verify
print(circuit_ref_list)
print(circuit_name_list)

parsed_circuit_refs = []
for item in circuit_ref_list:
    circuit_name = item
    circuit_ref_parsed = circuit_name.replace('_', ' ')
    parsed_circuit_refs.append(circuit_ref_parsed)


for item in parsed_circuit_refs:
    if item in circuit_ref_list:
        print("Circuit referentie", "'", item, "'", "komt voor in de circuitnaam. ")