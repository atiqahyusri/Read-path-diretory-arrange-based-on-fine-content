#Name = Wan Nur Atiqah Binti Wan Ahmad Yusri

import os

#function for read directory
def read_dir(dir):
    colection_filePath = []
    for root, dirs, files in os.walk(dir):
        for file in files:
            path_file = os.path.join(root, file)
            colection_filePath.append(path_file)
    return colection_filePath

#Ask directory from user and call function read dir
user_path = input('Please enter directory path:')
readUser_path = read_dir(user_path)

#start read content for each file in directory and append in a list
content_eachFile = []
for path in readUser_path:
    with open(path, 'r') as f:
        file_content = f.read()
        content_eachFile.append(file_content)

#convert element in list to int.
content_eachFile = [int(i) for i in content_eachFile]

#zip 2 list (file name and content) and start sorting
ziplist = list(zip(content_eachFile,readUser_path))
sorted_pairs = sorted(ziplist)
tuples = zip(*sorted_pairs)
content_eachFile, readUser_path = [ list(tuple) for tuple in  tuples]

#get file name only ignore the file extension, path
print('Output:', end = '')
for x in readUser_path:
    base = os.path.basename(x)
    os.path.splitext(base)
    #os.path.splitext(base)[0]
    print(os.path.splitext(base)[0], end = '')