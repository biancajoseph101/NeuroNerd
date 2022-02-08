-- settings.sql
CREATE DATABASE neuro;
CREATE USER neurouser WITH PASSWORD 'neuro';
GRANT ALL PRIVILEGES ON DATABASE neuro TO neurouser;