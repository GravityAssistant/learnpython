import os

def renameFiles():
    allFiles = os.listdir(r"E:\gitrepos\learnpython\prank")
    print(allFiles)

    for file in allFiles:
        noDigits = str.maketrans("", "", "0123456789")
        os.rename(file, file.translate(noDigits))

    print(allFiles)

renameFiles()
