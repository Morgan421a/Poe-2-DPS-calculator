CREATE TABLE Crossbows (
    name VARCHAR(255) NOT NULL,
    total_dps NUMERIC(6, 2) NOT NULL,
    crit_chance NUMERIC(4, 2) NOT NULL,
    attacks_per_second NUMERIC(4, 2) NOT NULL,
    reload_time NUMERIC(4, 2) NOT NULL,
    quality NUMERIC(5,2),
    item_level NUMERIC(4) NOT NULL,
    required_level NUMERIC(4) NOT NULL,
    rarity VARCHAR(255) NOT NULL
);