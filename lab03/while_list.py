#task 5
#mylist = [7,3,5,34,6]

#defining the list
mylist=[1,-1,-1,34,2,11]
#assigningning 0 to x to mark the start of the list count
x = 0
#creating a condition so that the while loop runs until it is False
while x < len(mylist):
    #adding 1 to each value in the list
    y = mylist[x] + 1
    #incrementing the position in the list by 1
    x = x + 1
    #returning new value in the list (when 1 is added)
    print y


