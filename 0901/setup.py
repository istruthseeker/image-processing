import os

answer = input("Preparing input is loading, accept ? Y is acceptable choice:  ")
if answer == 'Y' or answer == 'y':
    os.system('./1.py')
else:
    print("Preparing input is cancelled.")
