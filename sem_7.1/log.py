
def input_write(data: str):
    road = r'file.txt'
    with open(road,'w') as f:
        f.write(data)
