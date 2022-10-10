import pickle


with open("human.data", "rb") as file:
    lst = pickle.load(file)
print(lst)
