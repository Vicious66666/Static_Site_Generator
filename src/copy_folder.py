import os
import shutil

def copy_directory_recursive(source, destination):
    # 1. Clean the destination directory first
    if os.path.exists(destination):
        print(f"Cleaning destination: {destination}...")
        #shutil.rmtree(destination)
    
    # Create a fresh destination directory
    os.makedirs(destination)
    print(f"Created directory: {destination}")

    # 2. Start the recursive copy process
    if not os.path.exists(source):
        raise ValueError(f"Source path {source} does not exist.")

    def recursive_copy(src_path, dest_path):
        # List all items in the current source directory
        items = os.listdir(src_path)

        for item in items:
            s = os.path.join(src_path, item)
            d = os.path.join(dest_path, item)

            if os.path.isdir(s):
                # If it's a directory, create it in dest and recurse
                print(f"Creating directory: {d}")
                os.makedirs(d, exist_ok=True)
                recursive_copy(s, d)
            else:
                # If it's a file, copy it and log it
                print(f"Copying file: {s} -> {d}")
                shutil.copy(s, d)

    # Kick off the recursion
    recursive_copy(source, destination)

# Usage
#if __name__ == "__main__":
#    copy_directory_recursive("static", "public")