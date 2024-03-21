# Goodreads Book Scraper

Django project for scraping book information from Goodreads.com and storing it in a database. Users can view the scraped book data through a web interface.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Endpoints](#endpoints)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This Django project scrapes book information from Goodreads.com and stores it in a database. It provides a web interface to view the scraped book data.

## Features

- **Scraping Books**: Scrapes book information from Goodreads.com.
- **Storing in Database**: Stores scraped book data in a database using Django models.
- **Web Interface**: Provides a web interface to view the scraped book data.
- **Management Commands**: Includes custom Django management commands for scraping and populating the database.

## Installation

To run the Goodreads Book Scraper locally, follow these steps:

1. **Clone the repository**:

    ```bash
    git clone <https://github.com/MohammadRezaeian1997/goodreads_project.git>
    cd goodreads_project
    ```

2. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

3. **Apply migrations**:

    ```bash
    python manage.py migrate
    ```

4. **Scrape and populate the database**:

    ```bash
    python manage.py populate_books
    ```

5. **Run the development server**:

    ```bash
    python manage.py runserver
    ```

6. **Access the web interface**:

    Open your web browser and go to `http://localhost:8000/books/` to access the web interface for viewing scraped book data.

## Usage

- **View Book Data**: Navigate to `http://localhost:8000/books/` to view the list of scraped books.
- **Scrape and Populate Database**: Run the `populate_books` management command to scrape book data from Goodreads and populate the database.
- **Customization**: Modify the scraping logic in `books/scrape.py` to scrape additional information from Goodreads if needed.

## Project Structure
goodreads_project/
├── books/ # Django app for book-related functionality
│ ├── migrations/ # Database migrations
│ ├── management/ # Custom management commands
│ │ └── commands/ # Management commands
│ │ └── populate_books.py # Command to populate the database
│ ├── templates/ # HTML templates
│ │ └── books/ # Template directory for book-related views
│ │ └── book_list.html # Template for displaying book list
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── models.py # Django model for Book
│ ├── scrape.py # Web scraping functionality
│ ├── tests.py
│ ├── urls.py # URL configuration
│ └── views.py # Views for book-related functionality
├── goodreads_project/ # Django project directory
│ ├── init.py
│ ├── settings.py # Django settings file
│ ├── urls.py # URL configuration
│ └── wsgi.py
├── manage.py # Django management script
└── requirements.txt # List of dependencies


## Endpoints

- **View Book List**: `/books/` (GET)
- **Scrape and Populate Database**: `/populate_books/` (POST)

## Contributing

Contributions to Goodreads Book Scraper are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature`)
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature`)
6. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

"""
    return readme_content

# Generate README.md content
readme_content = generate_readme()

# Write content to a README.md file
with open("README.md", "w") as file:
    file.write(readme_content)

print("README.md generated successfully.")


