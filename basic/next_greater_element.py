''' Next greater element'''


def next_greater_element(arr):
    stack=[]
    for x in arr:
        stack.append(x)
    while stack:
        print (stack.pop())

def main():
    arr = [1,2,4,5]
    next_greater_element(arr)

main()    
