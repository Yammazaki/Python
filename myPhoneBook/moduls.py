import pickle #rick

#READ
def read_file(file):

    with open(file,'rb') as f:
        return pickle.loads(f.read())

#WRITE
def write_file(file,data):

    with open(file,'wb') as f:
        f.write(pickle.dumps(data))