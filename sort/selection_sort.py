def selection_sort():
    result=[]
    while len(lst)>0:
        print(result,lst)
        smallest=lst.index(min(lst))
        result.append(lst[smallest])
        lst.pop(smallest)
    return result
lst=[50,30,10,40,20]
print(selection_sort())