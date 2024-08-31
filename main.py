import json

# Initialize the books list
books = []
file_path = 'books.json'

def add_book():
    """Prompts the user to enter book details and adds the book to the list."""
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    summary = input("Summarize the essential thoughts from the book: ")
    
    book = {
        "title": title,
        "author": author,
        "summary": summary
    }
    
    books.append(book)

def save_books():
    """Saves the books list to a JSON file."""
    with open('books.json', 'w') as file:
        json.dump(books, file, indent=4)

def load_books():
    """Loads books from a JSON file if it exists."""
    global books
    try:
        with open('books.json', 'r') as file:
            books = json.load(file)
    except FileNotFoundError:
        books = []

def main():
    """Main loop for the program."""
    load_books()
    
    while True:
        print("\n1. Add a book")
        print("2. View books")
        print("3. Save and exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            add_book()
        elif choice == '2':
            for book in books:
                print(f"\nTitle: {book['title']}")
                print(f"Author: {book['author']}")
                print(f"Summary: {book['summary']}")
        elif choice == '3':
            save_books()
            print("Books saved. Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
