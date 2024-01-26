import pg8000

# Dit is de connectiefunctie voor de postgres database.
# Wijzig hier je port, password en database naam indien nodig
# Commit en push dit bestand niet!
def db_connection():
    conn = pg8000.connect(
        host="localhost",
        port=5434,
        user="postgres",
        password="farmainterim",
        database="f1_dataset"
    )
    cursor = conn.cursor()
    return conn, cursor