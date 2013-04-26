create schema  videonotes;

CREATE TABLE videonotes.notes
(
  pk bigint PRIMARY KEY NOT NULL,
  user varchar(30) NOT NULL,
  vid_fk bigint  NOT NULL,
  time int NOT NULL,
  text text  NOT NULL,
  ts timestamp NOT NULL default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP
) ENGINE=INNODB;
COMMIT;

CREATE TABLE videonotes.users
(
  pk bigint PRIMARY KEY NOT NULL,
  username varchar(30) NOT NULL,
  password varchar(30) NOT NULL,
  ts timestamp NOT NULL default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP
) ENGINE=INNODB;

CREATE TABLE videonotes.videos
(
  pk bigint  PRIMARY KEY NOT NULL,
  title varchar(100) NOT NULL,
  url varchar(150) NOT NULL,
  ts timestamp NOT NULL default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP
) ENGINE=INNODB;

