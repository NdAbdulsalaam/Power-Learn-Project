# File Creation
try:
    with open("my_file.txt", "w") as file:
        file.write("Hello, this is line 1.\n")
        file.write("12345\n")
        file.write("Line 3: End of file creation.\n")
    print("File 'my_file.txt' created successfully.")
except Exception as e:
    print(f"Error occurred while creating file: {e}")
finally:
    print("\n")

# File Reading and Display
try:
    with open("my_file.txt", "r") as file:
        print("Contents of 'my_file.txt':")
        print(file.read())
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied to read file.")
except Exception as e:
    print(f"Error occurred while reading file: {e}")
finally:
    print("\n")

# File Appending
try:
    with open("my_file.txt", "a") as file:
        file.write("This is line 4: Appended content.\n")
        file.write("67890\n")
        file.write("Line 6: End of appending.\n")
    print("Content appended to 'my_file.txt' successfully.")
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied to append to file.")
except Exception as e:
    print(f"Error occurred while appending to file: {e}")
finally:
    print("\n")

# Error Handling
try:
    with open("nonexistent_file.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied to read file.")
except Exception as e:
    print(f"Error occurred: {e}")
finally:
    print("\n")
