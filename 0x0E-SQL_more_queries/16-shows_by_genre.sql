-- List all shows and their linked genres (display NULL if no genre)
SELECT tv_shows.title, tv_genres.name
FROM tv_shows
LEFT JOIN tv_genres ON tv_shows.genre_id = tv_genres.id
ORDER BY tv_shows.title ASC, tv_genres.name ASC;
