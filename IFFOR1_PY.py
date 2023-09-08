'''
This script is code stub for CodeChef problem code IFFOR1_PY
Filename:      IFFOR1_PY_solution.py
Created:       27/09/2021
Last Modified: 27/09/2021
Author:        e-Yantra Team
'''

# Main function
if __name__ == '__main__':
    
    # Take the T (test_cases) input
    test_cases = int(input())

    # Write your code from here
    


    for i in range(0,test_cases):
      num = int(input())
      for j in range(0,num):
        if j==0:
          print(j+3,end=' ')
        elif j%2 == 0:
          print(j*2,end=' ')
        elif j%2 !=0:
          print(j**2,end=' ')
      print()