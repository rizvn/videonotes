/*
create schema  videonotes;

create user 'riz'@'localhost';

GRANT ALL ON videonotes.* TO 'riz'@'localhost' identified by 'pass';

REVOKE ALL PRIVILEGES, GRANT OPTION FROM 'riz'@'localhost';
drop user 'riz'@'localhost';
*/
DROP TABLE IF EXISTS notes;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS videos;
DROP TABLE IF EXISTS categories;

CREATE TABLE notes
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

CREATE TABLE users
(
  pk BIGINT PRIMARY KEY NOT NULL AUTO_INCREMENT,
  username VARCHAR(30) NOT NULL,
  password VARCHAR(32) NOT NULL,
  ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
  email VARCHAR(100) NOT NULL,
  sec_key VARCHAR(32)
)ENGINE=INNODB;
CREATE UNIQUE INDEX unique_email ON users ( email );
CREATE UNIQUE INDEX unique_username ON users (username);


CREATE TABLE videos
(
  pk bigint  PRIMARY KEY NOT NULL AUTO_INCREMENT,
  title varchar(100) NOT NULL,
  url varchar(150) NOT NULL,
  cat varchar(150),
  created_by varchar(30),
  share int default 0,
  ts timestamp NOT NULL default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP
) ENGINE=INNODB;

CREATE TABLE categories
(
  pk bigint  PRIMARY KEY NOT NULL AUTO_INCREMENT,
  name varchar(100) NOT NULL,
) ENGINE=INNODB;


/*------------------- Add Data -------------------------------*/
insert  into users (pk, username, email, password)
  values ('1', 'rizvan', 'riz@rizvn.com', 'password');

insert  into users (pk, username, email, password)
  values ('2', 'bob', 'bob@rizvn.com' ,'pass');

insert into videos(pk, title, url)
  values (1, 'Paradise - Coldplay', 'http://www.youtube.com/watch?v=1G4isv_Fylg');
