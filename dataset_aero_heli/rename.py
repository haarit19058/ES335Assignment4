import os

def rename_images(directory_path):
    files = [f for f in os.listdir(directory_path) if f.endswith('.jpg')]
    
    # Sort files to maintain order if needed
    files.sort()
    
    # Rename each file
    for i, filename in enumerate(files):
        # Create the new file name
        new_name = f"train_aero_{i}.jpg"
        
        # Get the full path for the old and new file names
        old_path = os.path.join(directory_path, filename)
        new_path = os.path.join(directory_path, new_name)
        
        # Rename the file
        os.rename(old_path, new_path)
        print(f"Renamed '{filename}' to '{new_name}'")

# Example usage
rename_images(r"dataset_aero_heli\train\aero")
