create database contatos;
use contatos;

create table contatos
(
	#cod_contatos int primary key auto_increment,
	email varchar(45) not null unique,
    assunto varchar(45) not null,
    descricao varchar(60) not null
);


describe contatos;

insert into contatos (email, assunto, descricao) values
('fatec@fatec.sp.gov.br','Fatec','Flask'),
('fatec1@fatec.sp.gov.br','Fatec','Banco de Dados');


select * from contatos;