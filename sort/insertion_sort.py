lst=[50,30,40,10,20]
def insertion_sort(lst):
    result=[]
    while len(lst)>0:
        print(result,lst)
        x=lst.pop(0)
        j=len(result)-1
        while j>=0 and result[j]>x:
            j-=1
        result.insert(j+1,x)
    return result
result=insertion_sort(lst)
print(result)
