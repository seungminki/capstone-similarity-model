CREATE DATABASE IF NOT EXISTS my_test_db;

CREATE TABLE my_test_db.posts (
    id INT AUTO_INCREMENT,
    post_id INT NOT NULL,
    board_id INT NOT NULL,
    content TEXT NOT NULL,
    user_id INT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
        ON DELETE SET NULL
        ON UPDATE CASCADE,
    PRIMARY KEY (id),
    UNIQUE KEY unique_post_board (post_id, board_id)
);

DROP TABLE IF EXISTS my_test_db.posts;

CREATE TABLE my_test_db.test_posts (
    id INT AUTO_INCREMENT,
    post_id INT,
    board_id INT,
    content TEXT,
    user_id INT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
        ON DELETE SET NULL
        ON UPDATE CASCADE,
    PRIMARY KEY (id)
);

CREATE TABLE my_test_db.users (
    user_id INT AUTO_INCREMENT,
    user_name VARCHAR(100) NOT NULL,
    PRIMARY KEY (user_id)
);