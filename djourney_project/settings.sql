-- settings.sql
CREATE DATABASE djourneys;
CREATE USER djourneyuser WITH PASSWORD 'password';
GRANT ALL PRIVILEGES ON DATABASE djourneys TO djourneyuser;