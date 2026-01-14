import re
def mini_library_system():
    try:
        title = input("Enter the book title: ")
        if not re.match(r'^[A-Za-z\s]+$', title):
            raise ValueError("Error: Book title must contain only alphabets and spaces.")
        year = input("Enter the publication year (YYYY): ")
        if not re.match(r'^(19|20)\d{2}$', year):
            raise ValueError("Error: Publication year must be a 4-digit number starting with '19' or '20'.")
        print(f"\nBook accepted ✅\nTitle: {title}\nYear: {year}")
    except ValueError as ve:
        print(ve)
    finally:
        print("\nProgram finished (with or without errors).")
mini_library_system()
