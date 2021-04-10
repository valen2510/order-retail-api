-- Set up databse tables

CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
DROP TYPE IF EXISTS type;
CREATE TYPE type AS ENUM('Credit Card', 'Debit Card', 'Cash');

-- users table
CREATE TABLE IF NOT EXISTS users (
    id uuid DEFAULT uuid_generate_v4(),
    name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    gov_id INTEGER UNIQUE NOT NULL,
    email VARCHAR(80) UNIQUE,
    company VARCHAR(80),
    PRIMARY KEY (id)
);

-- countries table
CREATE TABLE IF NOT EXISTS countries (
    id SERIAL,
    country_name VARCHAR(50) NOT NULL,
    cost_shipping INTEGER NOT NULL,
    PRIMARY KEY (id)
);

-- states table
CREATE TABLE IF NOT EXISTS states (
    id SERIAL,
    state_name VARCHAR(50) NOT NULL,
    country_id INTEGER NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (country_id) REFERENCES countries(id)
);

-- cities table
CREATE TABLE IF NOT EXISTS cities (
    id SERIAL,
    city_name VARCHAR(50) NOT NULL,
    state_id INTEGER NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (state_id) REFERENCES states(id)
);

-- shipping table 
CREATE TABLE IF NOT EXISTS shipping (
    id SERIAL,
    user_id uuid NOT NULL,
    address VARCHAR(80) UNIQUE NOT NULL,
    city_id INTEGER NOT NULL,
    state_id INTEGER NOT NULL,
    country_id INTEGER NOT NULL,
    cost INTEGER NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (city_id) REFERENCES cities(id),
    FOREIGN KEY (state_id) REFERENCES states(id),
    FOREIGN KEY (country_id) REFERENCES countries(id)
);

-- orders table 
CREATE TABLE IF NOT EXISTS orders (
    id SERIAL,
    user_id uuid NOT NULL,
    shipping_id INTEGER NOT NULL,
    order_date DATE,
    subtotal INTEGER,
    taxes INTEGER NOT NULL,
    total INTEGER,
    paid BOOLEAN NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (shipping_id) REFERENCES shipping(id)
);

-- Payment table 
CREATE TABLE IF NOT EXISTS Payments (
    id uuid DEFAULT uuid_generate_v4(),
    order_id INTEGER NOT NULL,
    payment_type type,
    payment_date DATE,
    total INTEGER,
    status BOOLEAN NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(id)
);

-- -- Populate  countries, states and cities table.
INSERT INTO countries (country_name, cost_shipping)
VALUES
    ('Argentina', 10),
    ('Belize', 10),
    ('Bolivia', 5),
    ('Brazil', 5),
    ('Canada', 20),
    ('Chile', 10),
    ('Colombia', 5),
    ('Costa Rica', 5),
    ('Cuba', 15),
    ('Ecuador', 5),
    ('El Salvador', 10),
    ('United states', 15),
    ('Guatemala', 10),
    ('Mexico', 10),
    ('Panama', 5),
    ('Paraguay', 5),
    ('Peru', 5),
    ('Uruguay', 10),
    ('Venezuela', 5);

INSERT INTO states (state_name, country_id)
VALUES
    ('Buenos Aires', 1),
    ('Cordoba', 1),
    ('Salta', 1),
    ('Belize Distric', 2),
    ('Santa Cruz', 3),
    ('La Paz', 3),
    ('Sao Paulo', 4),
    ('Rio de Janeiro', 4),
    ('Ontario', 5),
    ('Quebec', 5),
    ('Santiago Metropolitan', 6),
    ('Valparaiso', 6),
    ('Antofagasta', 6),
    ('Cundinamarca', 7),
    ('Antioquia', 7),
    ('Valle del Cauca', 7),
    ('San Jose', 8),
    ('Havana', 9),
    ('Guayas', 10),
    ('Pichincha', 10),
    ('San Salvador Metropolitan Area', 11),
    ('California', 12),
    ('Texas', 12),
    ('Florida', 12),
    ('Guatemala', 13),
    ('Mexico City', 14),
    ('Baja California', 14),
    ('Jalisco', 14),
    ('Panama', 15),
    ('Asuncion', 16),
    ('Lima', 17),
    ('Arequipa', 17),
    ('Montevideo', 18),
    ('Caracas', 19),
    ('Zulia', 19);


INSERT INTO cities (city_name, state_id)
VALUES
    ('Buenos Aires', 1),
    ('La Plata', 1),
    ('Mar de Plata', 1),
    ('Cordoba', 2),
    ('Rio Cuarto', 2),
    ('Salta', 3),
    ('Belize City', 4),
    ('Santa Cruz de la Sierra', 5),
    ('El Alto', 6),
    ('La Paz', 6),
    ('Sao Paulo', 7),
    ('Campinas', 7),
    ('Rio de Janeiro', 8),
    ('Sao de Caxias', 8),
    ('Toronto', 9),
    ('Ottawa', 9),
    ('Montreal', 10),
    ('Quebec', 10),
    ('Santiago', 11),
    ('Maipu', 11),
    ('Viña del Mar', 12),
    ('Antofagasta', 13),
    ('Bogota', 14),
    ('Medellin', 15),
    ('Rionegro', 15),
    ('Cali', 16),
    ('Buenaventura', 16),
    ('San Jose', 17),
    ('Havana', 18),
    ('Guayaquil', 19),
    ('Quito', 20),
    ('San Salvador', 21),
    ('Los Angeles', 22),
    ('San Diego', 22),
    ('San Francisco', 22),
    ('Austin', 23),
    ('Houston', 23),
    ('Dallas', 23),
    ('Miami', 24),
    ('Jacksonville', 24),
    ('Guatemala City', 25),
    ('Mexico City', 26),
    ('Tijuana', 27),
    ('Mexicali', 27),
    ('Guadalajara', 28),
    ('Zapopan', 28),
    ('Panama City', 29),
    ('Asuncion', 30),
    ('Lima', 31),
    ('Arequipa', 32),
    ('Montevideo', 33),
    ('Caracas', 34),
    ('Maracaibo', 35),
    ('Cabimas', 35);
