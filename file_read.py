# File Read & Write Challenge 🖋️
# Error Handling Lab 🧪

def modify_content(text):
    """Simple function to modify file content."""
    # Example modification: convert to uppercase
    return text.upper()

def main():
    try:
        # Ask user for input filename
        input_file = input("Enter the filename to read: ")

        # Try opening and reading the file
        with open(input_file, "r") as file:
            content = file.read()

        # Modify the content
        modified_content = modify_content(content)

        # Write to a new file
        output_file = "modified_" + input_file
        with open(output_file, "w") as file:
            file.write(modified_content)

        print(f"✅ File processed successfully! Modified version saved as '{output_file}'")

    except FileNotFoundError:
        print("❌ Error: The file does not exist. Please check the filename and try again.")
    except PermissionError:
        print("❌ Error: You don’t have permission to read this file.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
