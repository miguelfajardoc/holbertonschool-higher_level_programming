-- not my genres
SELECT tv_genres.name FROM (SELECT tv_genres.name AS dname FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id JOIN tv_genres
ON tv_show_genres.genre_id = tv_genres.id WHERE tv_shows.title = "Dexter")
AS dexter RIGHT JOIN tv_genres
ON dexter.dname = tv_genres.name WHERE dexter.dname IS NULL ORDER BY 1 ASC;
