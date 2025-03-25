import json # Import the json module

# define the file name
FileName = "data.json"

# Function to load books from the file 
def load_books():
    try:
        with open (FileName , "r") as File:
            return json.load(File)
    except (FileNotFoundError,json.JSONDecodeError):
        return []

# Function to save books to the file
def save_books(books):
    with open(FileName, "w") as File:
        json.dump(books, File,indent= 4)

# Function to get inputs from the user
def get_inputs(prompt):
    return input(prompt).strip()

# Function to add a book
def add_book(books):
    print("\tADD A BOOK\n")
    books.append({
        "title": get_inputs("Enter the title: "),
        "author": get_inputs("Enter the author: "),
        "year": int(get_inputs("Enter the year: ")),
        "genre": get_inputs("Enter the genre: "),
        # Get the read status from the user and convert it to a boolean value
        "read-status": get_inputs("Have you read this book? (yes/no): ").lower().startswith("y")
    })
    save_books(books)
    print(f"\n Book has been added successfully! \n")

# Function to remove a book
def remove_book(books):
    print("\tREMOVE A BOOK\n")
    title = get_inputs("Enter the title of the book you want to remove: ")
    # Loop through the books and remove the book with the given title
    for book in books:
        if book["title"].lower() == title.lower():
            books.remove(book)
            save_books(books)
            print(f"\n Book has been removed successfully! \n")
            break
    else:
        print(f"\n Book not found! \n")

# Function to search for a book
def search_books(books):
    print("\tSEARCH A BOOK\n")
    title = get_inputs("Enter the title of the book you want to search: ")
    for book in books:
        # If the title of the book matches the given title, display the book
        if book["title"].lower() == title.lower():
            # Display the book  
            print(f"\n Title: {book['title']}\n Author: {book['author']}\n Year: {book['year']}\n Genre: {book['genre']}\n Read Status: {'Yes' if book['read-status'] else 'No'}\n")
            break
    else:
        print(f"\n Book not found! \n")
 
# Function to display all books
def display_books(books):
    print("\tDISPLAY A BOOK\n")
    if books:
        for book in books:
            print(f"""
                  \n Title: {book['title']}\n
                   Author: {book['author']}\n 
                   Year: {book['year']}\n 
                   Genre: {book['genre']}\n 
                   Read Status: {'Yes' if book['read-status'] else 'No'}\n""")
    else:
        print("\t No books found! \n")

# Function to display statistics
def display_staticties(books):
    print("\tDISPLAY STATISTICS\n")
    # Calculate the total number of books and the number of read books
    total_books = len(books)
    read = sum(book["read-status"] for book in books)
    # Display the statistics
    result = f"Total Books:{total_books}\n Read Books:{read} ({(read/total_books*100) if total_books else 0:.2f}% read)\n "

    print(result)

def main():
    # Load the books from the file
    books = load_books()
    # Dictionary to map the options to the functions
    options = {
        "1": add_book,
        "2": remove_book,
        "3": search_books,
        "4": display_books,
        "5": display_staticties,
    }
    while True:
        print("","1. Add a book", "2. Remove a book", "3. Search for a book", "4. Display all books", "5. Display statistics", "6. Quit" ,"", sep="\n")
        # Get the user's choice
        choice = get_inputs("Enter your choice: ")
        # If the choice is to quit, break out of the loop
        if choice == "6":
         break
        # Call the function based on the user's choice
        options.get(choice, lambda: print("Invalid choice!"))(books)
# Save the books to the file
if __name__ == "__main__":
    main()