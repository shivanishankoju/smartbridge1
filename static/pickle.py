import pickle
with open('gas.Pkl','rb')as file:
    data=pickle.load(file)
    print(data)
try:
    with open('gas.Pkl','rb')as file:
        data=pickle.load(file)
except FileNotFoundError:
    print("file not found")
except pickle.UnpicklingError:
    print("error unpickling the file")