import requests
from bs4 import BeautifulSoup

# The URL of the page we want to scrape
URL = "https://books.toscrape.com/"

print(f"Fetching content from: {URL}")

try:
    # Send a GET request to the URL
    response = requests.get(URL)
    response.raise_for_status() # Check for HTTP errors (like 404 or 500)

    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find ALL book articles on the page
    # Books are typically enclosed in <article class="product_pod"> tags
    all_books = soup.find_all('article', class_='product_pod')

    if all_books:
        print("\n--- Extracted Data ---")
        print("Titles of all books on the page:")
        for i, book in enumerate(all_books):
            try:
                # Inside each book article, the title is usually in an <h3> tag,
                # which contains an <a> tag with a 'title' attribute.
                title_element = book.find('h3').find('a')
                book_title = title_element['title'].strip() # Get the 'title' attribute and remove whitespace
                print(f"{i+1}. {book_title}")
            except AttributeError:
                print(f"Warning: Could not find title for book {i+1}. Skipping.")
            except Exception as e:
                print(f"An unexpected error occurred while parsing book {i+1}: {e}")
    else:
        print("No book articles found on the page.")

except requests.exceptions.RequestException as e:
    print(f"An error occurred while fetching the page: {e}")
except Exception as e:
    print(f"An unexpected error occurred during parsing: {e}")

print("\nScraping process finished.")
