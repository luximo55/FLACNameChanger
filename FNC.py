import os;

dirChoice = input("Choose Directory:")
os.chdir(dirChoice)
for x, folder in enumerate(os.listdir()):
    print(dirChoice + "/" + folder)
    os.chdir(dirChoice + "/" + folder)
    for count, file in enumerate(sorted(os.listdir())):
        fileName, ext = os.path.splitext(file)
        if (ext != '.flac') and (ext != '.mp3') and (ext != '.txt'):
            break
        songName = fileName.split('-')
        if count+1 < 10:
            fileName = '0' + str(count + 1) + ' -' + songName[1];
        else:
            fileName = str(count + 1) + ' -' + songName[1];
        new_name = f'{fileName}{ext}'
        os.rename(file, new_name)
        print("Changed file " + file + " to " + new_name)
