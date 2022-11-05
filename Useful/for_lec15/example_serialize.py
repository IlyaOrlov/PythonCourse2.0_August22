import pickle_employee_example1
import pickle


e1 = pickle_employee_example1.Employee('Ivan', 'Ivanov')
# res = pickle.dumps(e1)
# network.send(res)

DUMPFILE_NAME = 'dump.txt'
with open(DUMPFILE_NAME, 'wb') as f:
    pickle.dump(e1, f, protocol=pickle.HIGHEST_PROTOCOL)
