--не менее 8 исполнителей;
ALTER SEQUENCE artists_id_seq RESTART WITH 1;

insert into artists (name)
values
	('Mink Mussel Creek'),
	('The Clean'),
	('Talking Heads'),
	('X-Ray Spex'),
	('Agent Orange'),
	('Jimi Hendrix'),
	('Crumb'),
	('CAN');

--не менее 5 жанров;
ALTER SEQUENCE genres_id_seq RESTART WITH 1;

insert into genres (name)
values
	('Psych-rock'),
	('Indie rock'),
	('Alternative rock'),
	('New wave'),
	('Post-punk'),
	('Art pop'),
	('Funk rock'),
	('Krautrock');

--таблица связей исполнителей с жанрами
insert into artistsgenres (genre_id, artist_id)
values
	('1', '1'),
	('1', '6'),
	('2', '2'),
	('3', '2'),
	('4', '3'),
	('5', '3'),
	('6', '3'),
	('7', '3'),
	('8', '8');
	
--не менее 8 альбомов;
ALTER SEQUENCE albums_id_seq RESTART WITH 1;

insert into albums (name, release_year)
values
	('Talking Heads: 77', '1977'),
	('Fear of Music', '2018'),
	('Vehicle', '1990'),
	('Modern Rock', '1994'),
	('Unknown Country', '1996'),
	('Are You Experienced', '2019'),
	('Axis: Bold as Love', '1967'),
	('Electric Ladyland', '1968');

--таблица связей исполнителей с альбомами
insert into albumsartists (album_id, artist_id)
values
	('1', '3'),
	('2', '3'),
	('3', '3'),
	('4', '3'),
	('5', '3'),
	('6', '6'),
	('7', '6'),
	('8', '6');

--не менее 15 треков;
ALTER SEQUENCE tracks_id_seq RESTART WITH 1;

insert into tracks (name, duration, album_id)
values
	('Uh-Oh, Love Comes to Town', '00:02:48', '1'),
	('New Feeling', '00:03:09', '1'),
	('Tentative Decisions', '00:03:04', '1'),
	('Happy Day', '00:03:55', '1'),
	('I Zimbra', '00:03:09', '2'),
	('Mind', '00:04:13', '2'),
	('Paper', '00:02:39', '2'),
	('Cities', '00:04:10', '2'),
	('Air', '00:03:34', '2'),
	('Animals', '00:03:30', '2'),
	('My Electric Guitar', '00:03:03', '2'),
	('Drugs', '00:05:10', '2'),
	('My Foxy Lady', '00:03:10', '6'),
	('Manic Depression', '00:03:31', '6'),
	('Love or Confusion', '00:03:05', '6'),
	('Fire', '00:02:30', '6');

--не менее 8 сборников
ALTER SEQUENCE compilation_id_seq RESTART WITH 1;

insert into compilation (name, release_year)
values
	('The Psychedelic World of the 13th Floor Elevators', '2002'),
	('Sign of the 3 Eyed Men', '2018'),
	('Pandora Box', '1990'),
	('Dreams', '2079'),
	('Retrospective', '2020'),
	('Singles', '2018'),
	('A Musical History', '1967'),
	('Greatest Hits', '1968');

--таблица связей сборников с треками
insert into compilationtracks (track_id, compilation_id)
values
	('1', '1'),
	('2', '3'),
	('3', '3'),
	('4', '2'),
	('5', '3'),
	('6', '6'),
	('7', '6'),
	('8', '2'),
	('5', '8'),
	('6', '7'),
	('7', '6'),
	('8', '5'),
	('9', '3'),
	('10', '3'),
	('11', '3'),
	('12', '7'),
	('13', '6'),
	('14', '1'),
	('15', '6');