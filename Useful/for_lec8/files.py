f1 = open('some_dir/q', 'r')
f2 = open('some_dir/q2', 'w')
for i in f1:
    f2.write(i)
f2.close()
f1.close()
