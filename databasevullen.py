from pymongo import MongoClient

# Connectie naar mongodb en datacollectie
# Wijzig indien nodig je database naam (Deze naam hebben we onderling besproken voor mongodb)
mongodb = MongoClient()
mongo_db = mongodb['f1_dataset']

# Dit is om de data op te halen voor de collecties
mongo_circuits = mongo_db['circuits']
mongo_constructor_results = mongo_db['constructor_results']
mongo_constructor_standings = mongo_db['constructor_standings']
mongo_driver_standings = mongo_db['driver_standings']
mongo_drivers = mongo_db['drivers']
mongo_lap_times = mongo_db['lap_times']
mongo_pit_stops = mongo_db['pit_stops']
mongo_qualifying = mongo_db['qualifying']
mongo_races = mongo_db['races']
mongo_results = mongo_db['results']
mongo_status = mongo_db['status']
mongo_sprint_results = mongo_db['sprint_results']
mongo_season_list = mongo_db['season_list']
