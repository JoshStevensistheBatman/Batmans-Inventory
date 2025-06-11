with open("Notmyfile.txt", "w") as file: 
    file.write("This text is written into the file.\n") 
    file.write("The W mode overides the file if it exists.\n")
    print("File has been written successfuly.")