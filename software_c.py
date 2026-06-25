import math

def run(number):
    if number < 0:
        print(f"  [C - Sqrt] Can't sqrt negative! Returning 0.")
        return 0
    result = round(math.sqrt(number), 2)
    print(f"  [C - Sqrt] sqrt({number}) = {result}")
    return result
print("Done")
;
