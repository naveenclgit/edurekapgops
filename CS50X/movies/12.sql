SELECT title
FROM movies
WHERE id IN (SELECT movie_id
             FROM stars
             WHERE person_id = (select id from people where name = 'Johnny Depp')
             AND movie_id IN (SELECT movie_id FROM stars WHERE person_id = (select id from people where name = 'Helena Bonham Carter'))
             );
