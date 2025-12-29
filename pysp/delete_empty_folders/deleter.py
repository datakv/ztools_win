import os
import sys

def delete_empty_folders(path):
    """
    Recursively delete empty folders starting from the given path.
    Returns the count of folders deleted.
    """
    deleted_count = 0
    
    # Walk through the directory tree bottom-up (so we process children before parents)
    for root, dirs, files in os.walk(path, topdown=False):
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            
            try:
                # Check if the directory is empty
                if not os.listdir(dir_path):
                    os.rmdir(dir_path)
                    print(f"Deleted empty folder: {dir_path}")
                    deleted_count += 1
            except (OSError, PermissionError) as e:
                print(f"Error accessing {dir_path}: {e}")
    
    return deleted_count

if __name__ == "__main__":
    
    if len(sys.argv) != 2:
        print("Usage: python delete_empty_folders.py <directory_path>")
        sys.exit(1)
    
    target_path = sys.argv[1]
    print(target_path)
    
    if not os.path.isdir(target_path):
        print(f"Error: {target_path} is not a valid directory")
        sys.exit(1)
    
    print(f"Scanning for empty folders in: {target_path}")
    total_deleted = delete_empty_folders(target_path)
    print(f"\nDone. Deleted {total_deleted} empty folders.")
