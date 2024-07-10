-- 0-uniq_users.sql
-- Use the database
USE hbtn_0d_tvshows;

-- Create users table with unique email
CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255)
);

