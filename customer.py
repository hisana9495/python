header = """BOOKSTORE RECEIPT
-------------------
"""
item1 = "Book Title: {}\tPrice: ₹{}"
item2 = "Book Title: {}\tPrice: ₹{}"
line1 = item1.format("Python Basics", 450)
line2 = item2.format("Data Science Intro", 600)
total_price = 450 + 600
total_line = "TOTAL:\t₹{}".format(total_price)
thank_you = "\nTHANK YOU FOR SHOPPING WITH US!"
receipt = header + line1 + "\n" + line2 + "\n" + total_line + thank_you
print(receipt.upper())