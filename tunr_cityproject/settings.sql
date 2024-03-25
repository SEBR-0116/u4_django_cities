-- settings.sql
CREATE DATABASE cityproject;
CREATE USER cityprojectuser WITH PASSWORD 'password';
GRANT ALL PRIVILEGES ON DATABASE cityproject TO cityprojectuser;