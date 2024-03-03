import requests

def count_books_from_api():
    response = requests.get('https://api.example.com/books')
    books_data = response.json()
    return len(books_data)

# Example usage:
total_books = count_books_from_api()
print("Total books from API:", total_books)
