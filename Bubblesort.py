import random

def main():
    L = [12, 64, 21, 97, 19, 45, 73, 31, 39]

    print(L)
    #sort with bubble sort
    '''for i in range(len(L)):
        for j in range(len(L) - 1):
            if L[j]>L[j+1]:
               temp = L[j]
               L[j] = L[j+1]
               L[j+1]=temp
            print(L)'''
    while True:
        #sort with Random sort
        MaxPos = len(L) - 1
        J = []
        for i in range(len(L)):
            randomPos = random.randint(0,MaxPos)
            J.append(L[randomPos])

        isSorted= True
        print(J)
        for i in range(len(L) - 1):
            if J[i] > J[i+1]:
                isSorted = False

        if isSorted == True:
            break
if __name__  == "__main__":
    main()
