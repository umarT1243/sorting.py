
#BUBBLE SORT
list1 = [6, 3, 1, 76, 5, 2, 4] #list 
def bubble_sort(x): # function starts
  n = len(x) # n is the length of the list
  for i in range(n): # for loop starts
    for j in range(0, n-i-1): # compares numbers in lists and swaps them
      if x[j] > x[j+1]:
        x[j], x[j+1] = x[j+1], x[j] #swaps if wrong order, largest number to the end
  return print ("this is bubble sort : " , x) # list is printed.
(bubble_sort(list1)) # the sorted list is returned.



#SELECTION SORT

def selection_sort(y) : # function starts
  n = len(y) # n is the length of the list
  for i in range(n): # for loop starts
    min = i # mis is the first number to compare
    for j in range(i+1, n): # compares numbers in lists and swaps them
      if y[j] < y[min]:
        min = j # min is the smallest number
    y[i], y[min] = y[min], y[i] #swaps if wrong order, smallest number to the front
  return print ("this is selection sort : " , y) # list is printed.
(selection_sort(list1)) # the sorted list is returned.
