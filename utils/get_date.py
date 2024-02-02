from PIL import Image
import os, datetime

def get_date(file_path):
    # set file date to modification time
    file_date = os.path.getmtime(file_path)
    
    # Convert the modification time to a readable format
    file_date = str(datetime.datetime.fromtimestamp(file_date).date())

    return file_date

if __name__ == "__main__":
    file_path = "12-23/received_1170714280998687.webp"
    pic_date = get_date(file_path)
    print(pic_date)
