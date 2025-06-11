import csv

def main():
    try:
        f=open("emp.csv", "w", newline='')
        cw=csv.writer(f)
        cw.writerow(['empno', 'ename', 'salary'])
        cw.writerow(['101', 'Peter', '34000'])
        cw.writerow(['102', 'Hellen', '34500'])
        cw.writerow(['103', 'Mash', '29000'])
        cw.writerow(['104', 'Mail', '34500'])
        cw.writerow(['105', 'Azer', '32000'])
    except OSError:
        print('error in creating csv file')
    finally:
        f.close()
main()