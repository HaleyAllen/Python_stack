def selectionSort(list):
   for filler in range(len(list)-1,0,-1):
       maxspot=0
       for location in range(1,filler+1):
           if list[location]>list[maxspot]:
               maxspot = location
       temp = list[filler]
       list[filler] = list[maxspot]
       list[maxspot] = temp

nlist = [14,46,43,27,57,41,45,21,70]
selectionSort(nlist)
print(nlist)