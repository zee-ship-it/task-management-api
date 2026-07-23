DROP TABLE IF EXISTS tasks;
CREATE TABLE tasks (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
   done BOOLEAN DEFAULT FALSE
);
INSERT INTO tasks (title, done) VALUES
('Go to gym', false),
('Complete Assignment', true),
('Read a book', false);