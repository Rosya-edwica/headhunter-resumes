BEGIN TRANSACTION;

CREATE DATABASE resumes WITH ENCODING='UTF8' LC_CTYPE='en_US.UTF-8' LC_COLLATE='en_US.UTF-8' OWNER=postgres TEMPLATE=template0 CONNECTION LIMIT=-1

CREATE TABLE position(
    id integer not null,
    parent_id integer,
    level integer not null,
    title text not null,
    prof_area varchar(255), 
    other_names text,
    parsed boolean,
    primary key(id)
);

CREATE TABLE city(
    id_hh integer not null,
    id_edwica integer not null,
    name varchar(255) not null,
    id_rabota_ru varchar(255) ,
    primary key(name)
);

CREATE TABLE resume(
    id varchar(255) not null,
    position_id integer not null,
    city_id integer not null default 'Россия',
    city varchar(255) not null,
    title text not null,
    salary integer,
    currency varchar(10),
    specializations text,
    experience_in_months integer,
    languages text,
    skills text,
    date_update varchar(255),
    url varchar(255),

    primary key(id),
    foreign key(position_id) references position(id),
    foreign key(city_id) references city(id_edwica)
);

create table experience_step(
    resume_id varchar(255) not null,
    post varchar(255) not null,
    duration_in_months integer not null,
    interval varchar(255) not null,
    branch text,
    subbranch text,
    primary key(resume_id, interval, post),
    foreign key(resume_id) references resume(id) on delete cascade
);

create table education(
    resume_id varchar(255) not null,
    title text not null,
    direction text, 
    year_grade integer not null,
    primary key(resume_id, title, direction, year_grade),
    foreign key(resume_id) references resume(id) on delete cascade
);

create table additional(
    resume_id varchar(255) not null,
    title text not null,
    direction text, 
    year_grade integer not null,
    primary key(resume_id, direction, year_grade),
    foreign key(resume_id) references resume(id) on delete cascade
);

END TRANSACTION;