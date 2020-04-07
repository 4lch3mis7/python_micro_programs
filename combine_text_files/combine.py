import os

dir_list = os.listdir()
txt_list = []

for item in dir_list:
    try:
        ext = item.split('.')[1]
        if (ext == 'txt') or (ext == 'lst'):
            txt_list.append(item)
    except:
        pass

#print("\n", txt_list, "\n")

for item in txt_list:
    file = open(item, 'rb')

    # when we are appending first wordlist but combined wordlist already exist,
    # then exit the program
    if item == txt_list[0] and os.path.exists('combined.txt'):
        print("\n[!] File combined.txt already exist")
        break

    file_new = open('combined.txt', 'ab')
    file_new.write(file.read())

    file_new.close()
    print(f"Successfully appended {item}")




