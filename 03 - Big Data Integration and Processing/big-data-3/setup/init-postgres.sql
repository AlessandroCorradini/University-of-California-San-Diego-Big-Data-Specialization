CREATE TABLE buyclicks (
	timestamp TIMESTAMP WITHOUT TIME ZONE NOT NULL, 
	txid INTEGER NOT NULL, 
	usersessionid INTEGER NOT NULL, 
	team INTEGER NOT NULL, 
	userid INTEGER NOT NULL, 
	buyid INTEGER NOT NULL, 
	price FLOAT NOT NULL
);

CREATE TABLE gameclicks (
	timestamp TIMESTAMP WITHOUT TIME ZONE NOT NULL, 
	clickid INTEGER NOT NULL, 
	userid INTEGER NOT NULL, 
	usersessionid INTEGER NOT NULL, 
	isHit INTEGER NOT NULL, 
	teamid INTEGER NOT NULL, 
	teamLevel INTEGER NOT NULL
);

CREATE TABLE adclicks (
	timestamp TIMESTAMP WITHOUT TIME ZONE NOT NULL, 
	txid INTEGER NOT NULL, 
	usersessionid INTEGER NOT NULL, 
	teamid INTEGER NOT NULL, 
	userid INTEGER NOT NULL, 
	adid INTEGER NOT NULL, 
	adcategory VARCHAR(11) NOT NULL
);


delete from buyclicks;
delete from gameclicks;
delete from adclicks;

COPY buyclicks FROM '/home/cloudera/Downloads/big-data-3/buy-clicks.csv' DELIMITER ',' CSV HEADER;
COPY gameclicks FROM '/home/cloudera/Downloads/big-data-3/game-clicks.csv' DELIMITER ',' CSV HEADER;
COPY adclicks FROM '/home/cloudera/Downloads/big-data-3/ad-clicks.csv' DELIMITER ',' CSV HEADER;
