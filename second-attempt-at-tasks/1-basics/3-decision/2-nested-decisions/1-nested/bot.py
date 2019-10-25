
print("what type of book cover is that?(soft/hard)")

book_cover_hardness = str(input())
if (book_cover_hardness == "soft"):
    print("is the cover perfect bound?(yes/no)")
    book_cover_bound = str(input())
    if (book_cover_bound == "yes"):
        print("soft cover, perfect bound books are popular")
    elif (book_cover_bound == "no"):
        print("soft covers with coils or stiches are great for short books")
    else:
        print("incorect input")


elif (book_cover_hardness == "hard"):
    print("hard cover books can be more expensive!")
    
else:
    print("incorect input")
