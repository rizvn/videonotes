/*
create schema  videonotes;

create user 'riz'@'localhost';

GRANT ALL ON videonotes.* TO 'riz'@'localhost' identified by 'pass';

REVOKE ALL PRIVILEGES, GRANT OPTION FROM 'riz'@'localhost';
drop user 'riz'@'localhost';
*/

use videonotes;

DROP TABLE IF EXISTS notes;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS videos;
DROP TABLE IF EXISTS tags;

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
  tags varchar(150),
  created_by varchar(30),
  share int default 0,
  ts timestamp NOT NULL default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP
) ENGINE=INNODB;

CREATE TABLE tags
(
  pk bigint PRIMARY KEY NOT NULL AUTO_INCREMENT,
  name varchar(100) NOT NULL
) ENGINE=INNODB;


/*------------------- Add Data -------------------------------*/
insert  into users (pk, username, email, password)
  values ('1', 'rizvan', 'riz@rizvn.com', 'password');

insert  into users (pk, username, email, password)
  values ('2', 'bob', 'bob@rizvn.com' ,'pass');

insert into videos(pk, title, url, tags, created_by)
    values (2,'Sell Your Ideas the Steve Jobs Way', 'http://www.youtube.com/watch?v=0q-wvAIeUgk', 'Business', 'admin');

insert into videos(pk, title, url, tags, created_by)
    values (3,'Pitch Anything in 15 seconds', 'http://www.youtube.com/watch?v=phyU2BThK4Q', 'Business', 'admin');

insert into videos(pk, title, url, tags, created_by)
    values (5,'Evaluating a business Idea', 'http://www.youtube.com/watch?v=y9ClKzMq3n0', 'Business', 'admin');

insert into videos(pk, title, url, tags, created_by)
    values (2,'Sell Your Ideas the Steve Jobs Way', 'http://www.youtube.com/watch?v=0q-wvAIeUgk', 'Business', 'admin');

insert into videos(pk, title, url, tags, created_by)
    values (3,'Pitch Anything in 15 seconds', 'http://www.youtube.com/watch?v=phyU2BThK4Q', 'Business', 'admin');

insert into videos(pk, title, url, tags, created_by)
    values (6,'Introduction to Mac OS X, Cocoa Touch, Objective-C and Tools', 'http://www.youtube.com/watch?v=oesNwgHn1ws', 'Programming', 'admin');

insert into videos(pk, title, url, tags, created_by)
    values (7,'iPhone Programming Tutorial 2 - Building a Simple Calculator', 'http://www.youtube.com/watch?v=OT_Z3qxxSsI', 'Programming', 'admin');

insert into videos(pk, title, url, tags, created_by)
    values (8,'iPhone Programming Tutorial 3 - Objective-C ', 'http://www.youtube.com/watch?v=jdCDRpgExtc', 'Programming', 'admin');
