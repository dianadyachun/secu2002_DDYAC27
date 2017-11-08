#Partnering with Heather
# #TASK 1
#defining the loop_filter function
def loop_filter(my_list,n):
    #creating a new list to store filtered values
    my_filtered_list = []
    #creating a for loop to call values in my_list
    for x in my_list:
        #creting a condition for filtered values
        if x > n:
            #adding filtered values to the newly created filtered list
            my_filtered_list.append(x)
    #returning filtered list
    return my_filtered_list

#defining my_list and n
my_list = [1,2,7,8]
n = 5
#printing the function
print loop_filter(my_list,n)

#TASK 2
#define lambda_filter function using filter and lambda commands
lambda_filter = filter(lambda x: x > n, my_list)
#printing the lambda_filter function
print lambda_filter







