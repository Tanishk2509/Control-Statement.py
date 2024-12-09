# A transport company charges the fare according to following table:

def calculate_fare(distance):
    
    if 1 <= distance <= 50:
        fare = distance * 8  # 8 Rs. per km for 1-50 km
    elif 51 <= distance <= 100:
        fare = distance * 10  # 10 Rs. per km for 51-100 km
    elif distance > 100:
        fare = distance * 12  # 12 Rs. per km for more than 100 km
    else:
        return "Invalid distance. Distance should be positive."

    return fare

try:
    distance = float(input("Enter the distance traveled (in km): "))
    fare = calculate_fare(distance)
    
    if isinstance(fare, str):  
        print(fare)
    else:
        print(f"The total fare is: Rs. {fare:}")
except ValueError:
    print("Please enter a valid number for the distance.")
