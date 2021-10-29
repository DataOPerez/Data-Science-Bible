# Copy file to another

'''I found this example interesting as well. Usually we have to read the data inside a file.
But in this example it goes straight into writing the "readfile" into the "writefile"'''
with open('Example2.txt', 'w') as file:
      file.write('line 1 \n')
      file.write('line 2 \n')
      file.write('line 3 \n')

with open('Example2.txt','r') as readfile:
    with open('Example3.txt','w') as writefile:
          for line in readfile:
                writefile.write(line)

'''I just tested and it looks like it works. So im assuming the "with" keyword reads the whole file at the beginning.
'''