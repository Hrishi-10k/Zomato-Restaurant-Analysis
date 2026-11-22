CREATE DATABASE zomato_restaurant_analysis;
USE zomato_restaurant_analysis;

CREATE TABLE restaurants (
    restaurant_id INT PRIMARY KEY,
    restaurant_name VARCHAR(255),
    city VARCHAR(100),
    cuisines VARCHAR(500),
    has_online_delivery VARCHAR(10),
    aggregate_rating DECIMAL(3,2),
    votes INT,
    average_cost_for_two INT
);

SELECT COUNT(*) AS total_records
FROM restaurants;

-- Displaying 10 records
SELECT *
FROM restaurants
LIMIT 10;

-- Checking column structure
DESCRIBE restaurants;

-- Checking missing values
SELECT
    COUNT(*) AS total_records,
    SUM(cuisines IS NULL) AS missing_cuisines,
    SUM(restaurant_name IS NULL) AS missing_names,
    SUM(city IS NULL) AS missing_cities
FROM restaurants;

-- 1. Count restaurants city-wise.  
SELECT city, COUNT(*) AS total_restaurants
FROM restaurants
GROUP BY city
ORDER BY total_restaurants DESC;

-- 2. Find the highest-rated restaurants.
SELECT restaurant_name, city, aggregate_rating
FROM restaurants
ORDER BY aggregate_rating DESC
LIMIT 10;  

-- 3. Calculate average restaurant ratings.  
SELECT ROUND(AVG(aggregate_rating), 2) AS average_rating
FROM restaurants
WHERE aggregate_rating > 0;

-- 4. Count restaurants by cuisine.
SELECT cuisines, COUNT(*) AS restaurant_count
FROM restaurants
GROUP BY cuisines
ORDER BY restaurant_count DESC;  

-- 5. Find restaurants offering online delivery.
SELECT restaurant_name, city
FROM restaurants
WHERE has_online_delivery = 'Yes';  

-- 6. Calculate average cost for two by city.
SELECT city,
       ROUND(AVG(average_cost_for_two), 2) AS avg_cost
FROM restaurants
GROUP BY city
ORDER BY avg_cost DESC;  

-- 7. Rank restaurants by customer votes.
SELECT restaurant_name, city, votes,
       RANK() OVER (ORDER BY votes DESC) AS restaurant_rank
FROM restaurants;  

-- 8. Find restaurants with ratings above 4.5.
SELECT restaurant_name, city, aggregate_rating
FROM restaurants
WHERE aggregate_rating > 4.5
ORDER BY aggregate_rating DESC;  

-- 9. Count restaurants by price range.
SELECT price_range, COUNT(*) AS total_restaurants
FROM restaurants
GROUP BY price_range
ORDER BY price_range;  

-- 10. Identify the most popular cuisine.
SELECT cuisines, COUNT(*) AS restaurant_count
FROM restaurants
GROUP BY cuisines
ORDER BY restaurant_count DESC
LIMIT 1; 