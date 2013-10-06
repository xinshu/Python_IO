import os

## read the names of the files in a folder or folders
## output a list of filenams

## dir: a string of the directory path
def read_filenames(dir):
  outfile = open('output.txt', 'w')
  for dirpath, subdir, filenames in os.walk(dir):
    for name in filenames:
      outfile.write(name + '\n')
  outfile.close()
  
def main():
  dir = r'C:\Users\Documents\GitHub\Python_v_2.7.5'
  read_filenames(dir)
  
if __name__ == '__main__':
  main()