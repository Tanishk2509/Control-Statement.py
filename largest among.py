#python program to find the largest among three number.

def find_largest_three(numbers):
    
    if len(numbers) < 3:
        return "List must contain at least three numbers."
    
    
    sorted_numbers = sorted(numbers, reverse=True)
    largest_three = sorted_numbers[:3]
    
    return largest_three


numbers = [10, 4, 3, 50, 23, 90]
largest_three_numbers = find_largest_three(numbers)
print("The largest three numbers are:", largest_three_numbers)
