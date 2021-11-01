def selectionSort(list):
   for filler in range(len(list)-1,0,-1):
       maxspot=0
       for location in range(1,filler+1):
           if list[location]>list[maxspot]:
               maxspot = location
       temp = list[filler]
       list[filler] = list[maxspot]
       list[maxspot] = temp

list = [8,5,2,6,9,3,1,4,7]
selectionSort(list)
print(list)