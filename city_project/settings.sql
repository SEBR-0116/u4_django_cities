-- settings.sql
CREATE DATABASE Djourneys;
CREATE USER DjourneyUser WITH PASSWORD 'djourneys';
GRANT ALL PRIVILEGES ON DATABASE Djourneys TO DjourneyUser;