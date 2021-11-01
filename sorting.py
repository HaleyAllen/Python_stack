def selectionSort(list):
   for fillslot in range(len(list)-1,0,-1):
       maxpos=0
       for location in range(1,fillslot+1):
           if list[location]>list[maxpos]:
               maxpos = location
       temp = list[fillslot]
       list[fillslot] = list[maxpos]
       list[maxpos] = temp

nlist = [14,46,43,27,57,41,45,21,70]
selectionSort(nlist)
print(nlist)