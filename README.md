# This is my scratchpad for experimenting and learning with my brother.

### Things to consider:  when working with data (files vs. databases etc.)
# Acid  
* Atomicity: all or nothing
* Consistency: rules will be followed  ex. uniqueness of data 
* Isolation: if two threads touch the same data, who wins? eg. serializable
* Durability: like the pyramids, whatever you change is permanent

# A Possible Schema

| ID  | Topic     | Question                          | Answer       |
|-----|-----------|-----------------------------------|--------------|
| A1  | Databases | In ACID the "A" stands for        | Atomicity    |
| A2  | Databases | In ACID the "C" stands for        | Consistency  |
| A3  | Databases | In ACID the "I" stands for        | Isolation    |
| A4  | Databases | In ACID the "D" stands for        | Durability   |
| A5  | Trivia    | Brothers are precious             | Indeed       |


# Create statement for the above table
CREATE TABLE Q_and_A (
    id VARCHAR(10) PRIMARY KEY,
    topic TEXT,
    question TEXT,
    answer TEXT
);
# Sample inserts (thank you chat gpt)
INSERT INTO Q_and_A (id, topic, question, answer)
VALUES 
('A1', 'Databases', 'In ACID the "A" stands for', 'Atomicity'),
('A2', 'Databases', 'In ACID the "C" stands for', 'Consistency'),
('A3', 'Databases', 'In ACID the "I" stands for', 'Isolation'),
('A4', 'Databases', 'In ACID the "D" stands for', 'Durability'),
('A5', 'Trivia', 'Brothers are precious', 'Indeed');

# Example updates
UPDATE Q_and_A
SET answer = 'a color formed by mixing blue and red'
WHERE id = 'A6';

# Example queries
select * from Q_and_A where id='A6';
| id | topic  |    question     |   answer  |
----+--------+-----------------+-------------
| A6 | TRIVIA | What is purple? | brain magic |
