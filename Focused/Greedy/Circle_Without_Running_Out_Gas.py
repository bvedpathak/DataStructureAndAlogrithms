# 1 unit of gas takes you 1 mile
def where_to_start_to_complete_without_running_of_gas(gas, miles):
    if not gas or not miles:
        return -1
    # If the total gas is less than the total cost, completing the
    # circuit is impossible
    if sum(gas) < sum(miles):
        return -1
    
    start = tank = 0

    for i in range(len(gas)):
        tank += gas[i] - miles[i]

        # If your tank has negative gas, we can not continue through the circuit
        # from the current start point, nor from any station before or including 
        # the current station 'i'. So lets try the i + 1 station..
        if tank < 0:
            # Set the next station as the new start oint and rest the tank
            start = i + 1
            tank = 0    
    
    return start

gas =  [3, 2, 1, 3, 3, 2, 3, 4]
miles =[2, 1, 4, 1, 2, 6, 0, 3]

print("\n")
print(f"Where to start to complete the circule without running out of gas: {where_to_start_to_complete_without_running_of_gas(gas, miles)}")
