def create_file():
    filename=input("Enter File name:")
    try:
        with open(filename,"x"):
            print("File created successfully!")
            print("====================================")
            print()
    except:
        print("File already created!")

def write_file():
    filename=input("Enter File name:")
    data=input("enter data to write:")
    with open(filename,"w")as file:
        file.write(data+"\n")
    print("Data Written successfully!")
    print("==========================================")
    print()

def read_file():
    filename=input("Enter File name:")
    with open(filename,"r")as file:
        data=file.read()
    print("File content:\n")
    print(data)
    print("==============================================")

def append_file():
    filename=input("Enter File name:")
    data=input("enter data to be append:")
    with open(filename,"a")as file:
        file.write(data+"\n")
    print("data append successfully!")
    print("===================================================")

