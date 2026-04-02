-- Runs once automatically on first Postgres container boot.
-- Creates the transactions table, seeds it, then stamps the Alembic
-- version table so Alembic knows migration 0001 is already applied.

CREATE TABLE IF NOT EXISTS transactions (
    id           SERIAL PRIMARY KEY,
    date         DATE NOT NULL,
    description  VARCHAR(255) NOT NULL,
    amount       FLOAT NOT NULL,
    category     VARCHAR(100) NOT NULL,
    is_recurring BOOLEAN NOT NULL DEFAULT FALSE
);

-- Load seed data from the mounted CSV.
COPY transactions (date, description, amount, category, is_recurring)
FROM '/docker-entrypoint-initdb.d/seed.csv'
DELIMITER ','
CSV HEADER;

-- Tell Alembic this migration is already applied so it doesn't
-- try to re-create the table on backend startup.
CREATE TABLE IF NOT EXISTS alembic_version (
    version_num VARCHAR(32) NOT NULL,
    CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);
INSERT INTO alembic_version (version_num) VALUES ('0001')
ON CONFLICT DO NOTHING;
