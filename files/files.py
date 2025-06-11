#writing content to file

'''def main():
    try:
        f=open("test.txt","w")
        f.write('Armando is the next best programmer in the world')
    except OSError:
        print('Error in the creation of the file')
    finally:
        f.close()

main()'''

#reading content from a file
def main():
    f = None
    try:
        f = open("test.txt", "r")
        s = f.read()
        print(s)
    except OSError:
        print("file not found")
    finally:
        if f:
            f.close()

main()