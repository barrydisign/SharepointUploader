from sharepoint import SharePoint
import sys

# example : python3 sp-upload.py source-filename-and-path destination-filename sharepoint-folder


# Source file with path.
file_dir_path = str(sys.argv[1])
# Desination sharepoint file name.
file_name = str(sys.argv[2])
# The Sharepoint folder to upload to.
folder_name = str(sys.argv[3])


# upload file
SharePoint().upload_file(file_dir_path, file_name, folder_name)

# delete file
# SharePoint().delete_file(file_name, folder_name)

