import os


dirList = os.listdir()
fileList = []
combinedFile = 'combined.txt'
strippedFile = 'stripped.txt'


def getFileList():
    for item in dirList:
        try:
            ext = item.split('.')[1]
            if (ext == 'txt') or (ext == 'lst'):
                fileList.append(item)
        except:
            pass


    return(fileList)


def combineFiles():
    getFileList()
    for item in fileList:
        file = open(item, 'rb')

        if item == fileList[0] and os.path.exists(combinedFile):
            print(f"\n[!] File {combinedFile} already exists.")
            file.close()
            break

        newFile = open(combinedFile, 'ab')
        newFile.write(file.read())
        newFile.close()
        file.close()

        print(f'[+] Successfully appended {item}')

combineFiles()

def stripWordlist():
    file = open(combinedFile, 'rb')
    buffer = file.readlines()
    strippedList = list(dict.fromkeys(buffer))

    newFile = open(strippedFile, 'wb')
    newFile.writelines(strippedList)
    newFile.close()
    file.close()

    print('[+] File stripped and repeated words removed successfully.')
    print(f'[+] File saved as {strippedFile}')


if __name__ == '__main__':
    combineFiles()
    stripWordlist()










