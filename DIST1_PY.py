'''
This script is code stub for CodeChef problem code DIST1_PY
Filename:      DIST1_PY_solution.py
Created:       27/09/2021
Last Modified: 27/09/2021
Author:        e-Yantra Team
'''


# Import any required module/s


# Function to calculate Euclidean distance between two points
def compute_distance(x1, y1, x2, y2):
    distance = 0
    distance=((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    distance = round(distance,2)
    print('Distance',end=': ')
    print(distance)
    return distance
    # Complete this function to return Euclidean distance and
    # print the distance value with precision up to 2 decimal places


# Main function
if __name__ == '__main__':
    # Take the T (test_cases) input
    test_cases = int(input())

    # Write the code here to take the x1, y1, x2 and y2 values
    for i in range(0,test_cases):
        x1,y1,x2,y2 = input().split(' ')
        x1 = int(x1)
        x2 = int(x2)
        y1 = int(y1)
        y2 = int(y2)
        compute_distance(x1, y1, x2, y2)


    # Once you have all 4 values, call the compute_distance function to find Euclidean distance
