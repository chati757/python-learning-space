import inspect
import sys

def who_imported_me():
    if inspect.stack()[-1]:
        return inspect.stack()[-1].filename.split('\\')[-1]
    return None

# Test the function
if __name__ == "__main__":
    print("This file is being run directly.")
else:
    importer = who_imported_me()
    print(f"This file is being imported by: {importer}")