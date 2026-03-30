import os
import argparse

# basic demo
def average(nums):
    total = 0
    for n in nums:
        total += n
    return total / len(nums)

def print_demo(val:str)-> None:
    print(val)

data = [10, 20, 30, 40]
result = average(data)
print("Average:", result)


# add arg parser
parser = argparse.ArgumentParser()
parser.add_argument(
    "numbers",
    type=float,
    nargs="+",
    help="List of numbers"
)

args = parser.parse_args()


# add .env into launch json
print_demo(os.getenv("API_KEY","API KEY ENVIRONMENT VARIABLE DOES NOT EXIST"))