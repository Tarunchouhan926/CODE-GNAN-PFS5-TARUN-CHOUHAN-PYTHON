CREATE DATABASE resume_analyzer;

USE resume_analyzer;

CREATE TABLE candidates (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    location VARCHAR(255) NOT NULL,
    cgpa DECIMAL(3, 2),
    education_details TEXT,
    ats_score DECIMAL(5, 2)
);
select*from candidates;

