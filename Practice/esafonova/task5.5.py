with open('task5.5.1', 'r') as f:
  f_str = f.read()
f_str = f_str.replace('\t', '    ')

with open('task5.5.1', 'w') as file:
  file.write(f_str)

with open('task5.5.1', 'r') as f:
  f_str = f.read()
f_str = f_str.replace('    ', '\t')

with open('task5.5.1', 'w') as file:
  file.write(f_str)