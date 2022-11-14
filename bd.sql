create database Conta;
use Conta;

create table conta(
    Usuario varchar(50) not null,
    Senha varchar(50) not null
);
insert into conta values('Lulu', '3307');
select * from conta;