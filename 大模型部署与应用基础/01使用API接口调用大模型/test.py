def bubble_sort(alist):
    n = len(alist)
    for j in range(0,n-1):
        flag = False
        for i in range(0,n - 1 - j):
            if alist[i] > alist[i+1]:
                alist[i],alist[i+1] = alist[i+1],alist[i]
                flag = True
        if flag == False:
            return
        print(f'第{j + 1}趟:{l1}')


if __name__ == '__main__':
    l1 = [30,50,20,40,10]
    bubble_sort(l1)
    print(l1)