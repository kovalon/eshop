-- DDL
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

create table if not exists users (uuid UUID primary key not null default uuid_generate_v4(), 
							firstname varchar(50) not null, 
							surname varchar(50) not null, 
							middlename varchar(50),
							fio varchar(150) generated always as (surname || ' ' || firstname || ' ' || middlename) stored,
							sex char(1),
							age integer,
							constraint sex check (sex = 'M' or sex = 'F'));

create table if not exists orders (uuid uuid primary key not null default uuid_generate_v4(),
							number integer not null);
						
create table if not exists products (uuid uuid primary key not null default uuid_generate_v4(),
							name varchar(100) not null,
							description varchar(300),
							price varchar(50) not null,
							left_in_stock integer not null);

create table if not exists users2orders (uuid uuid primary key not null default uuid_generate_v4(),
										user_id uuid not null,
										order_id uuid not null,
										foreign key (user_id) references users(uuid),
										foreign key (order_id) references orders(uuid));
									
create table if not exists users2users (uuid uuid primary key not null default uuid_generate_v4(),
										follower_id uuid not null,
										following_id uuid not null,
										foreign key (follower_id) references users(uuid),
										foreign key (following_id) references users(uuid));
						
create table if not exists orders2products (uuid uuid primary key not null default uuid_generate_v4(),
											order_id uuid not null,
											product_id uuid not null,
											foreign key (order_id) references orders(uuid),
											foreign key (product_id) references products(uuid));

-- DML
insert into users (firstname, surname, middlename, sex, age) values ('John', 'Malkovich', 'Lebovksy', 'M', 50);
insert into users (firstname, surname, middlename, sex, age) values ('Lena', 'Markova', 'Antonovna', 'F', 50);

insert into orders (number) values (1);
insert into orders (number) values (2);

insert into products (name, description, price, left_in_stock) values ('apple', 'delicious fruit', '$0.50', 15);
insert into products (name, description, price, left_in_stock) values ('chocolate Lindt', 'swiss chocolate', '$1.50', 10);

select * from users;
select * from orders;
select * from products;
select * from users2orders;
select * from users2users;
select * from orders2products;

-- если нужно все удалить
--drop table users cascade;
--drop table orders cascade;
--drop table products cascade;
--drop table order2product cascade;
--drop table user2order cascade;