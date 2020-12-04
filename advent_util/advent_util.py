READWRITE_MODE = 'r'


# Reads file with given filename and returns the entire text of the file
def read_file(filename):
    file = open(filename, READWRITE_MODE)
    file_text = file.read()
    file.close()
    return file_text
