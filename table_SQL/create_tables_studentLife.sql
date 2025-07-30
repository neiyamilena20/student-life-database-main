DROP TABLE IF EXISTS academic_work;
DROP TABLE IF EXISTS mental_health;
DROP TABLE IF EXISTS person;
DROP TABLE IF EXISTS profession;
DROP TABLE IF EXISTS city;

-- Table des villes
CREATE TABLE city (
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

-- Table des professions
CREATE TABLE profession (
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

-- Table des personnes
CREATE TABLE person (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    gender VARCHAR(180) NOT NULL,
    age INT NOT NULL,
    city_id INT NOT NULL,
    profession_id INT NOT NULL,
    degree VARCHAR(255) NOT NULL,
    FOREIGN KEY (city_id) REFERENCES city(id),
    FOREIGN KEY (profession_id) REFERENCES profession(id)
);

-- Table santé mentale
CREATE TABLE mental_health (
    person_id BIGINT PRIMARY KEY,
    depression BOOLEAN NOT NULL,
    suicidal_thoughts BOOLEAN NOT NULL,
    sleep_duration VARCHAR(255) NOT NULL,
    family_history BOOLEAN NOT NULL,
    financial_stress INT NOT NULL,
    dietary_habits VARCHAR(255) NOT NULL,
    FOREIGN KEY (person_id) REFERENCES person(id)
);

-- Table académique / professionnelle
CREATE TABLE academic_work (
    person_id BIGINT PRIMARY KEY,
    academic_pressure INT NOT NULL,
    work_pressure INT NOT NULL,
    cgpa FLOAT NOT NULL,
    study_satisfaction INT NOT NULL,
    job_satisfaction INT NOT NULL,
    work_study_hours FLOAT NOT NULL, 
    FOREIGN KEY (person_id) REFERENCES person(id)
)