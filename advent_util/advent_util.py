READWRITE_MODE = 'r'


# Reads file with given filename and returns the entire text of the file
def read_file(filename='input'):
    file = open(filename, READWRITE_MODE)
    file_text = file.read()
    file.close()
    return file_text


# Takes the given list of patterns and makes them into this format: (pattern|pattern|pattern)
def re_join(*re_patterns):
    return '(%s)' % '|'.join(re_patterns)
