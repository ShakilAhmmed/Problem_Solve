# a11 = int(input("Enter A11 Element"))
# a12 = int(input("Enter A12 Element"))


# a21 = int(input("Enter A21 Element"))
# a22 = int(input("Enter A22 Element"))

# + - +
# - + -

a11 = 2
a12 = -1


a21 = 1
a22 = -2

data_set=[[a11,a12],[a21,a22]]
check_a = data_set[0][0] * data_set[1][1] - data_set[1][0] * data_set[0][1]
if check_a != 0 :
    print("Inverse Is Possible")
    array_count = 0
    for data in data_set:
        index_count = 0
        co_fact = []
        for number in data:
            # print(f"In Array {array_count} Number is {number} In Index {index_count}")
            if array_count == 0 and index_count==0:
                print(data_set[1][1])
            elif array_count == 0 and index_count==1:
                 print(data_set[1][0])
            elif array_count == 1 and index_count==0:
                 print(data_set[0][1])
            elif array_count == 1 and index_count==1:
                 print(data_set[0][0])
            index_count +=1
        array_count +=1 

            
            # print(number)
    # print(f"Co-Factor Of a11-{a11} is ")