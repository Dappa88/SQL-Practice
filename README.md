# SQL Problem-Solving with PostgreSQL and Python

![SQL Problem-Solving](https://th.bing.com/th/id/R.39a909f1cbd97767aa3c5383cefd80e2?rik=1ApUxsXKuIHGhA&pid=ImgRaw&r=0)

Welcome to the SQL Problem-Solving repository! This project showcases my solutions to various SQL questions from a textbook, implemented using PostgreSQL and Python. Through this repository, I demonstrate my proficiency in SQL, as well as my ability to connect to a PostgreSQL database using Python to solve complex problems.

## Table of Contents

- [Introduction](#introduction)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Contributing](#contributing)
- [License](#license)

## Introduction

As a data enthusiast, I embarked on this journey to tackle SQL problems and improve my problem-solving skills. This repository contains my solutions to various SQL questions from a textbook, showcasing my ability to design efficient queries and extract valuable insights from the database.

## Technologies Used

- **PostgreSQL**: A powerful open-source relational database management system known for its performance and scalability.
- **Python**: A versatile programming language that enables me to connect to the PostgreSQL database and execute queries.
- **psycopg2**: A Python adapter for PostgreSQL, allowing seamless integration between Python and the PostgreSQL database.

## Installation

To run the SQL problem-solving scripts, follow these steps:

1. Install PostgreSQL on your system if you haven't already. Refer to the PostgreSQL documentation for installation instructions: [PostgreSQL Official Website](https://www.postgresql.org/).

2. Clone this repository to your local machine:

```bash
git clone https://github.com/Dappa88/SQL-Practice.git
```

3. Install the required Python packages using `pip`:

```bash
pip install psycopg2
```

## Usage

To execute the SQL problem-solving scripts, follow these steps:

1. Ensure you have a running PostgreSQL server with a database created and relevant data loaded.

2. Update the database connection settings in the Python script (e.g., `connect_db.py`) to match your PostgreSQL configuration.

3. Run the Python script to execute the SQL queries:

```bash
python sql_problem_solving.py
```

4. The script will connect to the PostgreSQL database, execute the SQL queries, and display the results on the console.

## File Structure

The repository is organized as follows:

```
/
├── connect_db.py

├── Introductory
├── questions.py
├── Intermediate
├── questions.py
├── ...
└── README.md
```

- `db_connection.py`: Python script containing the database connection settings.
- `sql_problem_solving.py`: Python script to execute the SQL queries and display the results.
- `questions.py`, ...: SQL script files containing solutions to the textbook problems.

## Contributing

As this repository represents my individual solutions to the SQL problems, contributions are not open at this time. However, I appreciate feedback and suggestions for improvement.

## License

This project is licensed under the [MIT License](LICENSE), allowing you to use the code with proper attribution.

Thank you for exploring my SQL problem-solving journey with PostgreSQL and Python! 📚🐍
