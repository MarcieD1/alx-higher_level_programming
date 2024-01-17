-- List all Comedy shows in ascending order by show title
SELECT tv_shows.title
FROM tv_shows
JOIN tv_genres ON tv_shows.genre_id = tv_genres.id
WHERE tv_genres.name = 'Comedy'
ORDER BY tv_shows.title ASC;
