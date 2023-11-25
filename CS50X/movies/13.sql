SELECT name
FROM people, stars
WHERE people.id=stars.person_id
AND stars.movie_id IN (SELECT movie_id FROM stars WHERE person_id = (select id from people where name='Kevin Bacon' and birth=1958))
AND people.id != (select id from people where name='Kevin Bacon' and birth=1958);

