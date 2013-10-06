import sys

## input: 
"""
 _a_ var1 value1
_a- var2 value2
_a_ var3 value3
a var 4 value4
"""
## output:
"""
var1, var3
value1, value3
"""
def main():
  if len(sys.argv) != 3:
    print 'usage: ./read_0925.py file-to-read file-to-write'
    sys.exit(1)
    
  infile = open(sys.argv[1], 'r')
  var_list = []
  val_list = []
  for line in infile:
    w_list = line.rstrip().split()
    if w_list[0] == '_a_':
      var_list.append(w_list[1])
      val_list.append(w_list[2])
  infile.close()
  
  outfile = open(sys.argv[2], 'w')
  outfile.write(', '.join(var_list) + '\n')
  outfile.write(', '.join(val_list) + '\n')
  outfile.close()
  
if __name__ == '__main__':
  main()
  