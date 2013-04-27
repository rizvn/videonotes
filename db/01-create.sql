/*
create schema  videonotes;

create user 'riz'@'localhost';
use videonotes;
GRANT ALL ON videonotes.* TO 'riz'@'localhost' identified by 'pass';

REVOKE ALL PRIVILEGES, GRANT OPTION FROM 'riz'@'localhost';
drop user 'riz'@'localhost';
*/


CREATE TABLE videonotes.notes
(
  pk bigint PRIMARY KEY NOT NULL AUTO_INCREMENT,
  user varchar(30) NOT NULL,
  vid_fk bigint  NOT NULL,
  time int NOT NULL,
  text text  NOT NULL,
  share int default 0,
  ts timestamp NOT NULL default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP
) ENGINE=INNODB;
COMMIT;

CREATE TABLE videonotes.users
(
  pk bigint PRIMARY KEY NOT NULL AUTO_INCREMENT,
  username varchar(30) NOT NULL,
  password varchar(30) NOT NULL,
  ts timestamp NOT NULL default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP
) ENGINE=INNODB;



CREATE TABLE videonotes.users
(
  pk BIGINT PRIMARY KEY NOT NULL AUTO_INCREMENT,
  username VARCHAR(30) NOT NULL,
  password VARCHAR(30) NOT NULL,
  ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
  email VARCHAR(100) NOT NULL,
  pwd_rst_key VARCHAR(30) NOT NULL
)ENGINE=INNODB;a
CREATE UNIQUE INDEX unique_email ON users ( email );
CREATE UNIQUE INDEX unique_username ON users (username);


CREATE TABLE videonotes.videos
(
  pk bigint  PRIMARY KEY NOT NULL AUTO_INCREMENT,
  title varchar(100) NOT NULL,
  url varchar(150) NOT NULL,
  ts timestamp NOT NULL default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP
) ENGINE=INNODB;

