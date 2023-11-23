
#A Total des voitures par pays et par model

SELECT c.country, c.model, COUNT(*) AS total_cars
FROM consumer_data c
JOIN car_data d ON c.model = d.model AND c.year = d.year
GROUP BY c.country, c.model

#B Nombre de modèles le plus présent par pays

SELECT cd.model, cod.country, MAX(cod.sales_volume) AS max_sales_volume
FROM car_data cd
INNER JOIN consumer_data cod ON cd.model = cod.model AND cd.year = cod.year
GROUP BY cd.model, cod.country
HAVING MAX(cod.sales_volume) = (
    SELECT MAX(sales_volume)
    FROM consumer_data
    WHERE model = cd.model
)


#C Vérification si il y a un model de vendu au USA mais pas en France 

SELECT DISTINCT cd.model
FROM car_data cd
INNER JOIN consumer_data cod ON cd.model = cod.model AND cd.year = cod.year
WHERE cod.country = 'USA'
  AND cd.model NOT IN (
    SELECT model
    FROM consumer_data
    WHERE country = 'France'
  );


#D Coût moyen de chaque voiture par type de moteur dans chaque pays

SELECT c.country, d.engine_type, AVG(d.price) AS average_price
FROM consumer_data c
JOIN car_data d ON c.model = d.model AND c.year = d.year
GROUP BY c.country, d.engine_type


#E Note moyenne des voitures électriques par rapport aux voitures thermiques

SELECT engine_type, AVG(review_score) AS average_rating
FROM consumer_data c
JOIN car_data d ON c.model = d.model AND c.year = d.year
GROUP BY engine_type
