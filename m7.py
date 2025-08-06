def average(nums):
    count =0
    sum=0
    for i in nums:
        sum +=i
        count+=1
    return sum/count


numbers = [float(x) for x in input("Enter numbers separted by space ").split()]

print("miangine adad : ",average(numbers))