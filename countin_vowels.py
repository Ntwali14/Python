def main():
    try:
        f=open("test.txt","r")
        c=0
        while True:
            s=f.read(1)
            if s=="":
                break
            if s in "aeiouAEIOU":
                c=c+1
        print(f"Number of vowels in the file: {c}")
    except FileNotFoundError:
        print("file not found")
    finally:
        f.close()

main()