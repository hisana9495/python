paragraph = """Python is a popular programming language. 
This Python course helps beginners learn coding basics 
and understand how Python can be used in real-world projects."""
length = len(paragraph)
print("Length of paragraph (characters):", length)
print("First character:", paragraph[0])
print("Last character:", paragraph[-1])
print("Preview (first 50 chars):", paragraph[:50])
replaced = paragraph.replace("Python", "PYTHON")
print("\nParagraph with replacements:\n", replaced)
lowercase = paragraph.lower()
print("\nLowercase paragraph:\n", lowercase)
trimmed = paragraph.strip()
print("\nTrimmed paragraph:\n", trimmed)
words = trimmed.split()
print("\nList of words:\n", words)
if "course" in lowercase:
    print("\nThe word 'course' was found in the paragraph.")
final_message = "The course description is {} characters long and has {} words.".format(length, len(words))
print("\n" + final_message)