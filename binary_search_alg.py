#we first define binary search and we store the lists and elements in it 
def binary_search(list, element):
 #this variable is the middle part of the list which is equal to 0 
    middle = 0
#this variable represents the beginnign of the list and we store 0 in it 
    start = 0
#this variable represents the end of the list and it it stores the length of the list
    end = len(list)
#here we figure out how many steps does our code have to take to find the number it needs
    steps = 0
#this is a while loop that basically runs the binary algorithm
    while(start<=end):
        print("Step", steps, ":" , str(list[start:end+1]))
              
        steps = steps + 1
        middle = (start + end) // 2

        if element == list[middle]:
            return middle
        if element < list[middle]:
            end = middle -1 
        else:
            start = middle + 1
#if the programming finds nothing it return -1
    return - 1
#this is a lis tthat we created
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#this is the target of the list which is 2
target = 2
#this line basically the one that runs the program
binary_search(my_list, target)

            