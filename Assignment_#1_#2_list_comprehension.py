list = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
list2 = (1,2,3,4,5,6,7,8,9,10)
def even_odd() :
    obj = ["even" if item %2==0 else "odd" for item in range (20)]   
    print(obj)

def multiples() :
    multi = [ x*1 for x in list2 if x%3==0 ]
    print(multi)
    
even_odd()
multiples()