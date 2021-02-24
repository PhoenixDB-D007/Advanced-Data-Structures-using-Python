def Merge(Array):
    if len(Array) > 1:
        mid = len(Array)//2
        L = Array[:mid]
        R = Array[mid:]
        Merge(L)
        Merge(R) 
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                Array[k] = L[i]
                i += 1
            else:
                Array[k] = R[j]
                j += 1
            k += 1
 
        while i < len(L):
            Array[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            Array[k] = R[j]
            j += 1
            k += 1

def print_List(Array):
    for i in range(len(Array)):
        print(Array[i], end=" ")
    print()
 
if __name__ == '__main__':
    Array = [142, 811, 13, 52, 6, 745]
    print("Given Arrayay is", end="\n")
    print_List(Array)
    Merge(Array)
    print("Sorted Arrayay is: ", end="\n")
    print_List(Array)
