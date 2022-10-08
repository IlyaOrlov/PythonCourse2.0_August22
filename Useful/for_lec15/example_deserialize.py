import pickle

# obj = network.receive()

#obj = b'\x80\x04\x95B\x00\x00\x00\x00\x00\x00\x00\x8c\x08employee\x94\x8c\x08Employee\x94\x93\x94)\x81\x94}\x94(\x8c\x04name\x94\x8c\x04Ivan\x94\x8c\x07surname\x94\x8c\x06Ivanov\x94ub.'
#res = pickle.loads(obj)

DUMPFILE_NAME = 'dump.txt'
with open(DUMPFILE_NAME, 'rb') as f:
    res = pickle.load(f)

print(res)
print(res.name)
print(res.surname)
res.show_employee()
print(res.attr)

# e2 = type(res)('Petr', 'Petrov')
# print(e2.name)
# e2.show_employee()