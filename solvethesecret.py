import os

def renameFiles():
    workingDir = r"E:\gitrepos\learnpython\prank"
    
    allFiles = os.listdir(workingDir)
    print(allFiles)

    os.chdir(workingDir)
    print("Switched to new working dir: " + workingDir)

    for file in allFiles:
        noDigits = str.maketrans("", "", "0123456789")
        os.rename(file, file.translate(noDigits))

    allFiles = os.listdir(workingDir)
    print(allFiles)

renameFiles()
