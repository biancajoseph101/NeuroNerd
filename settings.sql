-- settings.sql
-- DROP DATABASE neuro;
CREATE DATABASE neuro;
CREATE USER nerduser WITH PASSWORD 'nerdpassword';
GRANT ALL PRIVILEGES ON DATABASE neuro TO nerduser;