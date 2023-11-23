
#docker-compose up -d
#docker-compose down



import pandas as pd 
from sqlalchemy import create_engine
import matplotlib.pyplot as plt


# Créer le moteur de connexion SQLAlchemy
engine = create_engine('postgresql://admin:admin@localhost:5432/test_db')

# Lire le premier fichier CSV
data1 = pd.read_csv('car_data.csv', delimiter=',', names=['make', 'model', 'year', 'price', 'engine_type'], skiprows=1)

# Insérer les données du premier fichier dans la table 'car_data' de la base de données
data1.to_sql('car_data', con=engine, if_exists='replace', index=False)

# Lire le deuxième fichier CSV
data2 = pd.read_csv('consumer_data.csv', delimiter=',', names=['country', 'brand', 'model', 'year', 'review_score', 'sales_volume'], skiprows=1)

# Insérer les données du deuxième fichier dans la table 'consumer_data' de la base de données
data2.to_sql('consumer_data', con=engine, if_exists='replace', index=False)

query = """
    SELECT cd.year,
        SUM(CASE WHEN cd.engine_type = 'Electric' THEN co.sales_volume ELSE 0 END) AS electric_cars,
        SUM(CASE WHEN cd.engine_type = 'Thermal' THEN co.sales_volume ELSE 0 END) AS thermal_cars
    FROM car_data cd
    JOIN consumer_data co ON cd.model = co.model AND cd.year = co.year
    WHERE cd.engine_type IN ('Electric', 'Thermal')
    GROUP BY cd.year
    ORDER BY cd.year
"""

data = pd.read_sql(query, con=engine)

print(data)
# Fermer la connexion au moteur
engine.dispose()


# Créer un graphique pour représenter les ventes de voitures électriques par rapport aux ventes de voitures thermiques par an
plt.figure(figsize=(10, 6))
plt.plot(data['year'], data['electric_cars'], label='Electric Cars')
plt.plot(data['year'], data['thermal_cars'], label='Thermal Cars')
plt.xlabel('Year')
plt.ylabel('Number of Cars Sold')
plt.title('Electric vs Thermal Cars Sold per Year')
plt.legend()
plt.grid(True)
plt.show()