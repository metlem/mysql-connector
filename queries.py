################
## DB QUERIES ##
################

db_queries = {
"create_table_query": """CREATE TABLE IF NOT EXISTS books (book_id INT NOT NULL AUTO_INCREMENT, book_name VARCHAR(200) NOT NULL, book_author VARCHAR(40) NOT NULL, book_publisher VARCHAR(200) NOT NULL, number_of_page INT NOT NULL, created_date DATE, PRIMARY KEY (book_id));""",

"insert_data_query": """INSERT INTO books (book_name, book_author, book_publisher, number_of_page, created_date) VALUES ('Kucuk Kara Balik', 'Samed Behrengi', 'Can Cocuk Yayinlari', 52, now());"""

}

