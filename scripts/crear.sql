--@C:\Users\Addiel\Desktop\LogsPrinting\src\scripts\crear.sql

connect user1/user1;

--CREATE table t1(a int, b int, c varchar(20))tablespace TS1;
insert into t1(a,b,c) values (1,1,'Hola soy u1'); 
insert into t1(a,b,c) values (1,2,'Adios tprueba1');
insert into t1(a,b,c) values (2,1,'Adios tprueba1');
insert into t1(a,b,c) values (22,11,'lol tprueba1');
insert into t1(a,b,c) values (25,14,'owo tprueba1');
insert into t1(a,b,c) values (28,17,'uwu tprueba1');
insert into t1(a,b,c) values (31,20,'u.u tprueba1');
insert into t1(a,b,c) values (34,23,'o.o tprueba1');
insert into t1(a,b,c) values (37,24,':v tprueba1');
insert into t1(a,b,c) values (40,27,'< . < tprueba1');
select a,b from t1;
select c,b from t1;
select c,a from tprueba1;
select a,c from t1;
select a,b,c from t1;
update t1 set a= 32 where b=1;
update t1 set a= 54 where b=2;

commit;
update t1 set a= 32 where a=2;
update t1 set a= 54 where b=1;
commit;
delete from t1 where a=32;
update t1 set a= 32 where b=1;
update t1 set a= 54 where b=2;
commit;

connect user2/user2;

--CREATE table t2(a int, b int, c varchar(20))tablespace TS2;
insert into t2(a,b,c) values (2,1,'Hola soy u2');
insert into t2(a,b,c) values (2,2,'Adios t2');
insert into t2(a,b,c) values (22,11,'lol tprueba1');
insert into t2(a,b,c) values (25,14,'owo tprueba1');
insert into t2(a,b,c) values (28,17,'uwu tprueba1');

select a,b from t2;
select c,b from t2;
select c,a from t2;
update t2 set a= 32 where b=1;
update t2 set a= 54 where b=2;
commit;
update t2 set a= 32 where a=2;
update t2 set a= 54 where b=1;
commit;
delete from t2 where a=32;
delete from t2 where b = 11;
delete from t2 where b = 1;
delete from t2 where b = 2;
update t2 set a= 32 where b=1;
update t2 set a= 54 where b=2;
commit;


connect user3/user3; 

--CREATE table t3(a int, b int, c varchar(20))tablespace TS3;
insert into t3(a,b,c) values (3,1,'Hola soy u3'); 
insert into t3(a,b,c) values (3,2,'Adios t3');
insert into t3(a,b,c) values (31,20,'u.u tprueba1');
insert into t3(a,b,c) values (34,23,'o.o tprueba1');
insert into t3(a,b,c) values (37,24,':v tprueba1');
insert into t3(a,b,c) values (40,27,'< . < tprueba1');
select a,b from t3;
select c,b from t3;
select c,a from t3;
update t3 set a= 3 where b=1;
update t3 set a= 4 where b=2;
commit;
update t3 set a= 323 where a=2;
update t3 set a= 5 where b=1;
commit;
delete from t3 where a=32;
update t3 set a= 33 where b=2;
update t3 set a= 54 where b=2;
commit;

connect user1/user1;
select * from t1;

connect user2/user2;
select * from t2;

connect user3/user3;
select * from t3;
commit;
--conn sys/k1n9r4d2 as sysdba;
--select * from v$log;
--alter system checkpoint;
--alter system switch logfile;