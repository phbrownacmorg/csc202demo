from typing import List

def class_status(hours:float) -> str:
    status:str = 'NO status: invalid input'
    if 0 <= hours < 24:
        status = 'freshman status'
    elif 24 <= hours < 56:
        status = 'sophomore status'
    elif 56 <= hours < 87:
        status = 'junior status'
    elif 87 <= hours:
        status = 'senior status'
    return status

def main(args:List[str]) -> int:
    hours:float = float(input('Please input a number of credit hours: '))
    print('A student with', hours, 'credit hours has', class_status(hours) + '.')
    return 0

if __name__ == '__main__':
    import sys
    main(sys.argv)