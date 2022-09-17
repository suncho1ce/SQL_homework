create table if not exists Genres (
	id serial primary key,
	name varchar(60) not null
);

create table if not exists Artists (
	id serial primary key,
	name varchar(60) not null
);

create table if not exists ArtistsGenres (
	genre_id integer references Genres(id),
	artist_id integer references Artists(id)
	--constraint pk primary key (genre_id, artist_id)
);

create table if not exists Albums (
	id serial primary key,
	name varchar(60) not null,
	release_year integer
);

create table if not exists AlbumsArtists (
	album_id integer references Albums(id),
	artist_id integer references Artists(id)
	--constraint pk primary key (album_id, artist_id)
);

create table if not exists Tracks (
	id serial primary key,
	name varchar(60) not null,
	duration time,
	album_id integer not null references Albums(id)
);

create table if not exists Compilation (
	id serial primary key,
	name varchar(60) not null,
	release_year integer
);

create table if not exists CompilationTracks (
	track_id integer references Tracks(id),
	compilation_id integer references Compilation(id)
	--constraint pk primary key (track_id, compilation_id)
);
