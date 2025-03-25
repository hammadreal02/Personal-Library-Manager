# Personal Library Manager

The **Personal Library Manager** is a Python-based application that allows users to manage their personal book collection. It provides functionalities to add, remove, search, display, and analyze books in a library. The application uses a JSON file (`data.json`) to store the book data persistently.

## Features

1. **Add a Book**  
    Add a new book to your library by providing details such as title, author, year, genre, and read status.

2. **Remove a Book**  
    Remove a book from your library by specifying its title.

3. **Search for a Book**  
    Search for a specific book in your library by its title and view its details.

4. **Display All Books**  
    View all the books in your library along with their details.

5. **Display Statistics**  
    Get statistics about your library, such as the total number of books and the percentage of books you have read.

6. **Persistent Storage**  
    All book data is stored in a JSON file (`data.json`), ensuring that your library is saved even after the application is closed.

## How to Use

1. Clone or download the repository to your local machine.
2. Ensure you have Python installed on your system.
3. Run the `app.py` file using the command:
    ```bash
    python app.py
    ```
4. Follow the on-screen menu to interact with the application:
    - `1`: Add a book
    - `2`: Remove a book
    - `3`: Search for a book
    - `4`: Display all books
    - `5`: Display statistics
    - `6`: Quit the application

## File Structure

- `app.py`: The main Python script containing the application logic.
- `data.json`: The JSON file used to store the book data.

## Example

Here is an example of how the application works:

1. **Adding a Book**  
    ```
    Enter the title: The Great Gatsby
    Enter the author: F. Scott Fitzgerald
    Enter the year: 1925
    Enter the genre: Fiction
    Have you read this book? (yes/no): yes
    ```

2. **Displaying Statistics**  
    ```
    Total Books: 1
    Read Books: 1 (100.00% read)
    ```

