if __name__ == '__main__':
    s = input()
    lst1 = [i.isalnum() for i in s]
    print(any(lst1))
    lst2 = [i.isalpha() for i in s]
    print(any(lst2))
    lst3 = [i.isdigit() for i in s]
    print(any(lst3))
    lst4 = [i.islower() for i in s]
    print(any(lst4))
    lst5 = [i.isupper() for i in s]
    print(any(lst5))
    
