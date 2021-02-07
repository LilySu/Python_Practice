SELECT id
FROM wine_region
WHERE
  price < (SELECT AVG(price) FROM wine_region)
ORDER BY id;

--You want to compare the calories in the 5 items with the largest number
--of calories, to the average number of calories in all items on offer.
--Create a new column avg_calories with the average over all of the data.

SELECT item, energy AS calories,
   AVG(energy) OVER() AS avg_calories
FROM food
ORDER BY calories DESC
LIMIT 5

--For each style return the price, alongside with the average price across
--all wines in the data.

SELECT style, price,
    ROUND(AVG(price) OVER(), 2) AS avg_price
FROM wine
ORDER BY style