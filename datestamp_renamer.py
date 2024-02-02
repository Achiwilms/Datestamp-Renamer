import os,argparse
from utils.get_date import get_date
from utils.rename_file import rename_file

def rename_files_by_date(file_dir):
    for filename in os.listdir(file_dir):
        # find extension
        _, extension = os.path.splitext(filename)

        # construct filepath
        filepath = os.path.join(file_dir, filename)
        
        # get creation date
        file_date = get_date(filepath)

        # construct new filepath
        new_path = os.path.join(file_dir, file_date+extension)

        # rename file
        rename_file(filepath, new_path)
    return   

if __name__ == "__main__":
    # read arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--file_dir', type=str, default='12-23', help='file directory to be renamed by date')
    args = parser.parse_args()
    # rename files
    rename_files_by_date(args.file_dir)