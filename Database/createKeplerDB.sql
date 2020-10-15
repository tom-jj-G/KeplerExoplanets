-- Database: kepler

-- DROP DATABASE kepler;

CREATE DATABASE kepler
    WITH 
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'C'
    LC_CTYPE = 'C'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;

COMMENT ON DATABASE kepler
    IS 'Kepler Exoplanets Bootcamp project team';