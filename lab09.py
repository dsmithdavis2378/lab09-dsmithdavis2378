# Problem-solving practice (LeetCode / ICPC style).
#
# For EACH problem, work out your problem-solving OUTLINE first - restate the problem,
# try a small example by hand, and sketch your approach - BEFORE you write or generate
# any code. You may use an AI assistant to help implement your plan (see the README),
# but do the thinking first.
#
# Do not rename the functions - the tests use these names.


def two_sum(nums, target):
    # Outline (write your plan here first):
    # First, I will use a loop to scan through the list of numbers. 
    # Then I will use another loop starting at i + 1 to ensure that i<j.
    # Lasly to obtain the target, I add the values of i and j, and retun the indices if they equal the target.
    #   ...
    # TODO: return the indices [i, j] (i < j) of the two numbers in `nums` that add up
    #   to `target`. Assume there is exactly one answer.

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            result = nums[i] + nums[j]
            if result == target:
                return [i, j]
            


def max_profit(prices):
    if not prices:
        return 0 
    # Outline:
    # Starting out I would create variables low and high to keep track of the lowest price to buy at and the highest possible profit.
    # Then I will use a loop to look through the prices at each day
    # If the price is less than the current low valuee, then the low value will be updated to the new price
    # If the difference between the price and the low value is greater than the current high, then the high value becomes the difference between the price and the low value.
    # Lastly, at the end of the program, the high price is returned for the greatest profit in the list
    #   ...
    # TODO: `prices[i]` is a stock price on day i. Return the most profit obtainable by
    #   buying on one day and selling on a LATER day. If no profit is possible, return 0.

    low = prices[0]
    high = 0
    for price in prices:
        if price < low:
            low = price
        if (price - low) > high:
            high = price - low
    return high


def max_subarray(nums):
    # Outline:
    # Firstly, I will create the variables current and highest to identify the current sum and the highest sum possible in the list.
    # Then, I will use a for loop beginning at the second index in order to find out whether the sum of the first value added to the next value is greater then the current sum.
    # If the sum is greater, the loop will continue adding through the list to try and fin the greatest sum for every combination in the list.
    # Lastly, once the sum is found highest is returned.
    #   ...
    # TODO: return the largest sum of any contiguous (in-a-row) block of numbers in
    #   `nums`. The list has at least one number.
    current = nums[0]
    highest = nums[0]

    for num in nums[1:]:
        current = max(num, current + num)

        if current > highest:
            highest = current

    return highest



def is_balanced(s):   # Part 4 - stretch (optional)
    stack = []
    match = {')': '(', ']': '[', '}': '{'}
    # Outline:
    # Firstly, I will create a stack variable to allow the last element to be removed
    # Then, I use a for loop to check if the brackets are closed in every element.
    # Lastly, is_balanced returns true if the brackets are closed, and false if they are not.
    #   ...
    # TODO: return True if every bracket in `s` is closed correctly and in the right
    #   order. The brackets are ( ) [ ] { }. (Hint: a list used as a stack works well.)
    for char in s:
        if char in match.values():
            stack.append(char)
        elif char in match:
            if not stack or stack[-1] != match[char]:
                return False
            stack.pop()
    return len(stack) == 0

        

    


def main():
    # Optional scratch space - try your functions here, then run: python lab09.py
    print(two_sum([2, 7, 11, 15], 9))   # [0, 1]
    print(max_profit([7, 1, 5, 3, 6, 4])) # [5]
    print(max_profit([7, 6, 4, 3, 1])) # [0]
    print(max_profit([])) # 0
    print(max_profit([1, 2])) # 1
    
    
    print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])) # 6
    print(max_subarray([1])) # 1
    print(max_subarray([5, 4, -1, 7, 8])) # 23


    print(is_balanced("()")) # True
    print(is_balanced("()[]{}")) # True
    print(is_balanced("(])")) # False
    


if __name__ == "__main__":
    main()
