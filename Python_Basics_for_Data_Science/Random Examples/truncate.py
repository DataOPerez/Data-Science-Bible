# create a new file with w mode and write three lines
with open('./truncate_data.txt', 'w') as data_file:
    data_file.write('Line 1\n')
    data_file.write('Line 2\n')
    data_file.write('Line 3\n')
    data_file.write('Line 4\n')

# open that file in r+ mode and perform tests
with open('truncate_data.txt', 'r+') as data_file:
    data = data_file.readlines() # read all the lines
    print(f'this is the data: {data}') # show the data
    print(f"Here's the cursor postion: {data_file.tell()}") # show the cursor postion

    data_file.seek(0, 0) # move cursor back to the beginning
    
    data_file.write('line a\n') # write two a new line
    data_file.write('line b\n') # '' 

    '''Notice that by writing these two new lines if we just read the file we start reading half way through.
    Also notice by writing those new lines that we overwrote line 1 & 2.
    Now uncomment the line of code below: '''

    #data_file.truncate()

    '''By definition the method will "truncate" the file size. If no argument is passed it uses the current
    position. 
    
    My understanding is that it reduces the file size given a location or by the current location. By
    reducing the file size we delete the data proceeds the position.'''

    data_file.seek(0, 0) # move the cursor back to the beginning again
    print(data_file.read()) # read all the lines again & print

    



