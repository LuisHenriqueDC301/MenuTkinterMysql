create database Conta;
use Conta;

create table conta(
    Usuario varchar(50) not null,
    Senha varchar(50) not null,
    constraint pk_Usu primary key (Usuario)
);
create table tarefas(
    Conta_Usuario varchar(50) not null,
    id int not null auto_increment, 
	tarefas varchar(100),
    data varchar(11),
	constraint pk_id primary key (id),
    constraint fk_C_U foreign key (Conta_Usuario) references conta(Usuario) on delete cascade
);
insert into conta values('Lulu', "3307");
insert into tarefas(Conta_Usuario,tarefas,data) values("Lulu", "Trabalho de biologia","25/11/2022");

select * from tarefas where Conta_Usuario = "Lulu";
delete from tarefas where Id = "3";