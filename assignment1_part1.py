def listDivide(numbers,divide=2):
    result=[]
    for i in numbers:
        if i%divide==0:
            result.append(i)
    return len(result)
class ListDivideException(Exception):
    pass
def testListDivide():
    if listDivide([1,2,3,4,5])!=2 or listDivide([2,4,6,8,10])!=5 or listDivide([30, 54, 63,98, 100], divide=10)!=2 or listDivide([])!=0 or listDivide([1,2,3,4,5], 1)!=5:
        raise ListDivideException("An error occurred")