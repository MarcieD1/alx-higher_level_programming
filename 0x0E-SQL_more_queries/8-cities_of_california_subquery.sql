-- List all cities of California from hbtn_0d_usa
SELECT cities.id, cities.name
FROM cities
WHERE cities.state_id IN (
  SELECT id FROM states WHERE name = 'California'
)
ORDER BY cities.id ASC;
