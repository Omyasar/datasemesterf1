import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from urllib.parse import unquote

urls_list = [
        "http://en.wikipedia.org/wiki/Melbourne_Grand_Prix_Circuit",
        "http://en.wikipedia.org/wiki/Sepang_International_Circuit",
        "http://en.wikipedia.org/wiki/Bahrain_International_Circuit",
        "http://en.wikipedia.org/wiki/Circuit_de_Barcelona-Catalunya",
        "http://en.wikipedia.org/wiki/Istanbul_Park",
        "http://en.wikipedia.org/wiki/Circuit_de_Monaco",
        "http://en.wikipedia.org/wiki/Circuit_Gilles_Villeneuve",
        "http://en.wikipedia.org/wiki/Circuit_de_Nevers_Magny-Cours",
        "http://en.wikipedia.org/wiki/Silverstone_Circuit",
        "http://en.wikipedia.org/wiki/Hockenheimring",
        "http://en.wikipedia.org/wiki/Hungaroring",
        "http://en.wikipedia.org/wiki/Valencia_Street_Circuit",
        "http://en.wikipedia.org/wiki/Circuit_de_Spa-Francorchamps",
        "http://en.wikipedia.org/wiki/Autodromo_Nazionale_Monza",
        "http://en.wikipedia.org/wiki/Marina_Bay_Street_Circuit",
        "http://en.wikipedia.org/wiki/Fuji_Speedway",
        "http://en.wikipedia.org/wiki/Shanghai_International_Circuit",
        "http://en.wikipedia.org/wiki/Aut%C3%B3dromo_Jos%C3%A9_Carlos_Pace",
        "http://en.wikipedia.org/wiki/Indianapolis_Motor_Speedway",
        "http://en.wikipedia.org/wiki/N%C3%BCrburgring",
        "http://en.wikipedia.org/wiki/Autodromo_Enzo_e_Dino_Ferrari",
        "http://en.wikipedia.org/wiki/Suzuka_Circuit",
        "https://en.wikipedia.org/wiki/Las_Vegas_Grand_Prix#Circuit",
        "http://en.wikipedia.org/wiki/Yas_Marina_Circuit",
        "http://en.wikipedia.org/wiki/Aut%C3%B3dromo_Oscar_Alfredo_G%C3%A1lvez",
        "http://en.wikipedia.org/wiki/Circuito_Permanente_de_Jerez",
        "http://en.wikipedia.org/wiki/Aut%C3%B3dromo_do_Estoril",
        "http://en.wikipedia.org/wiki/TI_Circuit",
        "http://en.wikipedia.org/wiki/Adelaide_Street_Circuit",
        "http://en.wikipedia.org/wiki/Kyalami",
        "http://en.wikipedia.org/wiki/Donington_Park",
        "http://en.wikipedia.org/wiki/Aut%C3%B3dromo_Hermanos_Rodr%C3%ADguez",
        "http://en.wikipedia.org/wiki/Phoenix_street_circuit",
        "http://en.wikipedia.org/wiki/Paul_Ricard_Circuit",
        "http://en.wikipedia.org/wiki/Korean_International_Circuit",
        "http://en.wikipedia.org/wiki/Aut%C3%B3dromo_Internacional_Nelson_Piquet",
        "http://en.wikipedia.org/wiki/Detroit_street_circuit",
        "http://en.wikipedia.org/wiki/Brands_Hatch",
        "http://en.wikipedia.org/wiki/Circuit_Zandvoort",
        "http://en.wikipedia.org/wiki/Zolder",
        "http://en.wikipedia.org/wiki/Dijon-Prenois",
        "http://en.wikipedia.org/wiki/Fair_Park",
        "http://en.wikipedia.org/wiki/Long_Beach,_California",
        "http://en.wikipedia.org/wiki/Las_Vegas_Street_Circuit",
        "http://en.wikipedia.org/wiki/Circuito_Permanente_Del_Jarama",
        "http://en.wikipedia.org/wiki/Watkins_Glen_International",
        "http://en.wikipedia.org/wiki/Scandinavian_Raceway",
        "http://en.wikipedia.org/wiki/Mosport",
        "http://en.wikipedia.org/wiki/Montju%C3%AFc_circuit",
        "http://en.wikipedia.org/wiki/Nivelles-Baulers",
        "http://en.wikipedia.org/wiki/Charade_Circuit",
        "http://en.wikipedia.org/wiki/Circuit_Mont-Tremblant",
        "http://en.wikipedia.org/wiki/Rouen-Les-Essarts",
        "http://en.wikipedia.org/wiki/Circuit_de_la_Sarthe#Bugatti_Circuit",
        "http://en.wikipedia.org/wiki/Reims-Gueux",
        "http://en.wikipedia.org/wiki/Prince_George_Circuit",
        "http://en.wikipedia.org/wiki/Zeltweg_Airfield",
        "http://en.wikipedia.org/wiki/Aintree_Motor_Racing_Circuit",
        "http://en.wikipedia.org/wiki/Circuito_da_Boavista",
        "http://en.wikipedia.org/wiki/Riverside_International_Raceway",
        "http://en.wikipedia.org/wiki/AVUS",
        "http://en.wikipedia.org/wiki/Monsanto_Park_Circuit",
        "http://en.wikipedia.org/wiki/Sebring_Raceway",
        "http://en.wikipedia.org/wiki/Ain-Diab_Circuit",
        "http://en.wikipedia.org/wiki/Pescara_Circuit",
        "http://en.wikipedia.org/wiki/Circuit_Bremgarten",
        "http://en.wikipedia.org/wiki/Pedralbes_Circuit",
        "http://en.wikipedia.org/wiki/Buddh_International_Circuit",
        "http://en.wikipedia.org/wiki/Circuit_of_the_Americas",
        "http://en.wikipedia.org/wiki/Red_Bull_Ring",
        "http://en.wikipedia.org/wiki/Sochi_Autodrom",
        "http://en.wikipedia.org/wiki/Baku_City_Circuit",
        "http://en.wikipedia.org/wiki/Algarve_International_Circuit",
        "http://en.wikipedia.org/wiki/Mugello_Circuit",
        "http://en.wikipedia.org/wiki/Jeddah_Street_Circuit",
        "http://en.wikipedia.org/wiki/Losail_International_Circuit",
        "http://en.wikipedia.org/wiki/Miami_International_Autodrome"
]

circuit_names_list = []

for item in urls_list:
    url = item
    parsed_url = urlparse(url)
    # Get the last part of the path (after the last '/')
    circuit_name = parsed_url.path.split('/')[-1] # Hier wordt circuit_name gesplit op '/' en wordt het laatste stukje
    # van elk item gepakt.
    circuit_name_parsed2 = circuit_name.split('_') # Hier wordt het laatste stukje gesplit op '_'.
    circuit_name_in_string = ' '.join(circuit_name_parsed2) # Hier maken we een string van het resultaat van circuit_name_parsed2
    print("Circuit Name:", circuit_name_in_string)
    circuit_names_list.append(circuit_name_in_string)

decoded_circuit_names = [unquote(circuit_name) for circuit_name in circuit_names_list] # Sommige characters zoals ó worden raar in de terminal geprint. Om dit op te lossen gebruiken
# we de unquote package om deze uitzonderingen goed in de output te krijgen.

location_list = [
        "Melbourne",
        "Kuala Lumpur",
        "Sakhir",
        "Montmeló",
        "Istanbul",
        "Monte-Carlo",
        "Montreal",
        "Magny Cours",
        "Silverstone",
        "Hockenheim",
        "Budapest",
        "Valencia",
        "Spa",
        "Monza",
        "Marina Bay",
        "Oyama",
        "Shanghai",
        "São Paulo",
        "Indianapolis",
        "Nürburg",
        "Imola",
        "Suzuka",
        "Las Vegas",
        "Abu Dhabi",
        "Buenos Aires",
        "Jerez de la Frontera",
        "Estoril",
        "Okayama",
        "Adelaide",
        "Midrand",
        "Castle Donington",
        "Mexico City",
        "Phoenix",
        "Le Castellet",
        "Yeongam County",
        "Rio de Janeiro",
        "Detroit",
        "Kent",
        "Zandvoort",
        "Heusden-Zolder",
        "Dijon",
        "Dallas",
        "California",
        "Nevada",
        "Madrid",
        "New York State",
        "Anderstorp",
        "Ontario",
        "Barcelona",
        "Brussels",
        "Clermont-Ferrand",
        "Quebec",
        "Rouen",
        "Le Mans",
        "Reims",
        "Eastern Cape Province",
        "Styria",
        "Liverpool",
        "Oporto",
        "California",
        "Berlin",
        "Lisbon",
        "Florida",
        "Casablanca",
        "Pescara",
        "Bern",
        "Barcelona",
        "Uttar Pradesh",
        "Austin",
        "Spielberg",
        "Sochi",
        "Baku",
        "Portimão",
        "Mugello",
        "Jeddah",
        "Al Daayen",
        "Miami"
]

def check_circuit_location(circuit_name, city):
    # Zoek de Wikipedia-link voor het circuit
    circuit_url = f"http://en.wikipedia.org/wiki/{circuit_name.replace(' ', '_')}"

    # Haal de HTML-pagina op
    response = requests.get(circuit_url)

    # Controleer of de pagina succesvol is opgehaald
    if response.status_code == 200:
        # Parse de HTML met BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Zoek naar de stad in de inhoud van de pagina
        if city.lower() in soup.get_text().lower():
            return f"{circuit_name} bevindt zich in {city}."
        else:
            return f"{circuit_name} bevindt zich niet in {city}."
    else:
        return f"Fout bij het ophalen van de Wikipedia-pagina voor {circuit_name}."

# Loop over de lijsten en voer de controle uit
for circuit_name, location in zip(decoded_circuit_names, location_list):
    result = check_circuit_location(circuit_name, location)
    print(result)
'''
This Python script does the following:

    1. It defines a list of URLs, each corresponding to a Wikipedia page for a Formula 1 Grand Prix circuit.

    2. It extracts the names of the circuits from the URLs. This is done by parsing the URLs using the urlparse function from the urllib.parse module. 
    The last part of the path (after the last '/') is taken and split on '_' to obtain the circuit name. The circuit name is then joined into a string.

    3. The script decodes the circuit names using unquote to handle special characters.

    4. It defines a list of locations (cities) corresponding to each circuit.

    5. It defines a function check_circuit_location that takes a circuit name and a city and checks if the Wikipedia page for that circuit mentions the city. 
    It uses the requests library to fetch the HTML content of the Wikipedia page and BeautifulSoup for parsing the HTML.

    6. Finally, it loops through the pairs of decoded circuit names and locations, calls the check_circuit_location function for each pair, and prints the result.

In summary, the script verifies if the Wikipedia page for each Grand Prix circuit mentions the correct location (city) based on the provided list of cities. 
It serves as a simple example of web scraping and data extraction from HTML using Python libraries. 
'''
