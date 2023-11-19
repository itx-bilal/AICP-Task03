electricity_matrix = [
    [550, 650, 750],
    [10, 15, 20],
    [100, 200, 300]
]

student_id = "XY12345678"

def costSlab1():
    print("Bill for slab 1 is")
    for cost in electricity_matrix[0]:
        print(cost, end="\t")
    print()

def costSlab2():
    print("Bill for slab 2 is")
    for cost in electricity_matrix[1]:
        print(cost, end="\t")
    print()

def costSlab3():
    print("Bill for slab 3 is")
    for cost in electricity_matrix[2]:
        print(cost, end="\t")
    print()

while True:
    print(f"My Student ID is {student_id}")
    print("Enter your choice")
    print("Press 1 to display the bill of slab 1 and slab 2.")
    print("Press 2 to display the bill of slab 3.")
    print("Press any other key to exit.")
    
    choice = input()

    if choice == '1':
        costSlab1()
        costSlab2()
    elif choice == '2':
        costSlab3()
    else:
        print("Program terminated.")
        break
