
try:
   
    with open("my_file.txt", "w") as file:
        
        file.write("Line 1: Hello, this is the first line.\n")
        file.write("Line 2: The number of apples is 5.\n")
        file.write("Line 3: Python file handling is fun!\n")
    print("File created and initial content written successfully.")
except PermissionError:
    print("Error: You do not have permission to write to this file.")
finally:
    print("Write operation complete.")


try:
 
    with open("my_file.txt", "r") as file:
        content = file.read()
        print("\nFile content after write operation:")
        print(content)
except FileNotFoundError:
    print("Error: File not found.")
finally:
    print("Read operation complete.")


try:
  
    with open("my_file.txt", "a") as file:
       
        file.write("Line 4: Adding more content to the file.\n")
        file.write("Line 5: The number 42 is significant.\n")
        file.write("Line 6: Appending works just fine.\n")
    print("\nAdditional content appended successfully.")
except PermissionError:
    print("Error: You do not have permission to append to this file.")
finally:
    print("Append operation complete.")


try:

    with open("my_file.txt", "r") as file:
        updated_content = file.read()
        print("\nFile content after appending:")
        print(updated_content)
except FileNotFoundError:
    print("Error: File not found.")
finally:
    print("Final read operation complete.")
