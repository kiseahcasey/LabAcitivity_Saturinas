def compute_lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y

    while True:
        if (greater % x == 0) and (greater % y == 0):
            lcm = greater
            break
        greater += 1

    return lcm

try:
    x = int(input("Enter a value for x: "))
    y = int(input("Enter a value for y: "))

    if x <= 0 or y <= 0:
        print("Error: Please enter only positive non-zero integers.")
    else:
        lcm = compute_lcm(x, y)
        print(f"The L.C.M. of {x} and {y} is {lcm}")

except ValueError:
    print("Invalid input. Please enter integers only.")