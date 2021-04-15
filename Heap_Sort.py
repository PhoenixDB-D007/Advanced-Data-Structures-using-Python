#Heap Sort Program

def heapsort( aList ):
  # convert aList to heap
  length = len( aList ) - 1
  leastParent = int(length / 2)
  for i in range ( leastParent, -1, -1 ):
    moveDown( aList, i, length )

  # flatten heap into sorted array
  for i in range ( length, 0, -1 ):
    if aList[0] > aList[i]:
      swap( aList, 0, i )
      moveDown( aList, 0, i - 1 )


def moveDown( aList, first, last ):
  largest = 2 * first + 1
  while largest <= last:
    # right child exists and is larger than left child
    if ( largest < last ) and ( aList[largest] < aList[largest + 1] ):
      largest += 1

    # right child is larger than parent
    if aList[largest] > aList[first]:
      swap( aList, largest, first )
      # move down to largest child
      first = largest;
      largest = 2 * first + 1
    else:
      return # force exit


def swap( A, x, y ):
  A[x],A[y] = A[y],A[x]


#User input
sort_list = list()
count = input("Enter number of elements : ")

print
print ('Enter '+str(count) +' numbers : ')

print
for i in range(int(count)):
    n = input("number"+str(i+1)+": ")
    sort_list.append(int(n))

heapsort(sort_list)

print
print ("Elements in sorted order :")
print(sort_list)
