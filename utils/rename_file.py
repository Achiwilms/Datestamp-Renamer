import os

def rename_file(old_path, new_path):
    # If the new name already exists, generate a unique name
    if os.path.exists(new_path):
        video_dir = os.path.dirname(new_path)
        base_name, extension = os.path.splitext(new_path.split("/")[-1])
        counter = 1
        while True:
            unique_path = os.path.join(video_dir, f"{base_name}_{counter}{extension}")
            if not os.path.exists(unique_path):
                break
            counter += 1
        new_path = unique_path
    os.rename(old_path, new_path)
    print(f"File {old_path} renamed to {new_path}")
    return
