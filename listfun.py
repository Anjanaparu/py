def find_sum(numbers):
    total=0
    for num in numbers:
        total += num
        return total
    n=int(input("Enter the number of elements:"))
    numbers=[]
    for i in range(n):
        value=int(input(f"enter number{i+1};"))
                        numbers.append(value)
                        result=find_sum(numbers)
                        print("sum of the all numbers in the list is:",result)
    
