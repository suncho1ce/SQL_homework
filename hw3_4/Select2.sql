--количество исполнителей в каждом жанре;
select name, count(artist_id) from artistsgenres a
join genres g on a.genre_id = g.id
group by g."name";


--количество треков, вошедших в альбомы 2019-2020 годов;
select release_year, count(t.id) from albums a
join tracks t on a.id = t.album_id
where release_year between 2019 and 2020
group by release_year;


--средняя продолжительность треков по каждому альбому;
select a.name, avg(duration) from albums a 
join tracks t on a.id = t.album_id
group by a."name";


--все исполнители, которые не выпустили альбомы в 2020 году;
select a.name from artists a 
full join albumsartists a2 on a.id = a2.artist_id 
full join albums a3 on a3.id = a2.album_id 
where a.id not in (select artist_id from albumsartists full join albums on albumsartists.album_id = albums.id where release_year = 2020)
group by a."name";

	--достаём айди исполнителей, которые выпустили альбомы в 2020
select artist_id from albumsartists
full join albums on albumsartists.album_id = albums.id
where release_year = 2020;


--названия сборников, в которых присутствует конкретный исполнитель (выберите сами);
select distinct c."name" from compilation c 
join compilationtracks c2 on c2.compilation_id = c.id
join tracks t on t.id = c2.track_id 
join albums a on a.id  = t.album_id 
join albumsartists a2 on a2.album_id = a.id 
join artists a3 on a3.id = a2.artist_id 
where a3."name" = 'Jimi Hendrix';


--название альбомов, в которых присутствуют исполнители более 1 жанра;
select a."name" from albums a 
join albumsartists a2 on a2.album_id = a.id 
	--пробуем пропустить таблицу
	--join artists a3 on a3.id = a2.artist_id 
join artistsgenres a3 on a3.artist_id = a2.artist_id 
join genres g on g.id = a3.genre_id 
where g."id" > 1
group by a."name";


--наименование треков, которые не входят в сборники;
select name from tracks t 
left join compilationtracks c on c.track_id = t.id
where c.compilation_id is null;


--исполнителя(-ей), написавшего самый короткий по продолжительности трек (теоретически таких треков может быть несколько);
select a."name" from artists a 
join albumsartists a2 on a2.artist_id = a.id 
join tracks t on t.album_id = a2.album_id 
where t.duration = (select min(duration) from tracks t2);


--название альбомов, содержащих наименьшее количество треков.
select a."name" from albums a 
join tracks t on t.album_id = a.id 
where t.album_id in (select album_id from tracks
group by album_id
having count(id) = (select count(id) from tracks
group by album_id
limit 1))
group by a."name" 

	--наименьшее число треков равно 4
select count(id) from tracks
group by album_id
limit 1

	--список айди альбомов с минимальным числом треков
select album_id from tracks
group by album_id
having count(id) = (select count(id) from tracks
group by album_id
limit 1)
