use videonotes;
insert  into videonotes.users (pk, username, password)
values ('1', 'riz', 'riz@rizvn.com', 'pass');

insert  into videonotes.users (pk, username, email, password)
values ('2', 'bob', 'bob@rizvn.com' ,'pass');

insert into videonotes.videos(pk, title, url)
values (1, 'Paradox of choice - Barry Scwhartz', '/static/testVideos/paradox_of_choice.mp4');

insert into videonotes.videos(pk, title, url)
values (2, 'Paradise - Coldplay', 'http://www.youtube.com/watch?v=1G4isv_Fylg');