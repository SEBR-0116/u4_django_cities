-- settings.sql
CREATE DATABASE djourney;
CREATE USER djourneyuser WITH PASSWORD 'djourney';
GRANT ALL PRIVILEGES ON DATABASE djourney TO djourneyuser;