books_data = [
    ("978-0143128540", "The Alchemist", "Paulo Coelho", "Fiction", 3),
    ("978-0439023528", "The Hunger Games", "Suzanne Collins", "Fiction", 5),
    ("978-0307277671", "Guns, Germs, and Steel", "Jared Diamond", "History", 2)
]

# Select the first book from the dataset and assign its individual attributes to separate variables
isbn = books_data[0][0]
#print(isbn)
title = books_data[0][1]
#print(title)
author = books_data[0][2]
#print(author)
genre = books_data[0][3]
#print(genre)
copies = books_data[0][4]
#print(copies)

'''Convert copies from integer to string. Take the copies variable, which is an integer, and convert it to a string using str(). 
Store the result in a new variable. Print both the original integer and the converted string.
'''
copiesStr = str(copies)
print(f"copies: {copies}, {type(copies)}\ncopiesStr: {copiesStr}, {type(copiesStr)}")
print("-----------------------------------------------------------------------------------------------------")

# Work with a list of genres. Start with a list containing "Fiction" and "History" as genres. 
# Use the append() method to add "Science" to the list. Print the updated genre list.
genreList = ["Fiction", "History"]
genreList.append("Science")
print(genreList)
print("-----------------------------------------------------------------------------------------------------")


#Select the second book tuple from books_data:
#("978-0439023528", "The Hunger Games", "Suzanne Collins", "Fiction", 5)
#Use indexing to print the book title, which is the second item, and the genre, which is the fourth item, from this tuple.
print(f"Title: {books_data[1][1]}\nGenre: {books_data[1][3]}")
print("-----------------------------------------------------------------------------------------------------")


# Create a dictionary named book_info with the following key-value pairs based on one book:
# Print the entire dictionary. Then access and print the value for the "author" key.
book_info = {
    "title": "Guns, Germs, and Steel",
    "author": "Jared Diamond",
    "genre": "History",
    "copies": 2
}
print(book_info["author"])
print("-----------------------------------------------------------------------------------------------------")

#Work with unique genres using a set: Create a set called unique_genres and add genres from all three books: 
#"Fiction" and "History". Add a new genre "Biography" using the add() method. Print the updated set of genres.
unique_genres = {"Fiction", "Fiction", "History"}
unique_genres.add("Biography")
print(unique_genres)
