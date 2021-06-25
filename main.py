import os
# asking the user for the path
path = input('Enter the path where you want to create the file: ')
# changing to the path the user entered
try:
    os.chdir(path)
except:
    print('Invalid path')
    quit()
# getting the file name
filename = input(f'Enter the file name you want to create in {path}: ')
# asking if they want to write anything
inp = input('Do you want to write something in the file?: ')
if inp.lower() == 'yes':
    # what they want to write
    write_to_file = input('What do you want to write in the file?: ')
    # creating and writing
    try:
        with open(filename, 'w') as filew:
            filew.write(write_to_file)
            filew.close()
    except:
        print('You can\'t write to {}'.format(filename))
else:
    quit()
