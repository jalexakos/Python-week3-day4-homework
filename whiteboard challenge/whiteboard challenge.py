"""
Find smallest number  - (Without min)
Create a function that given a list of numbers (non-sorted) find the lowest number in the list and return it.
Example Input: [50,30,4,2,11,0]
Example Output: 0
Example Input 2: [40,3,4,2]
Example Output 2: 2
"""

# Questions to ask:
# Are numbers always positive?
# Is there a max num we will potentially be fed? Solved for this using max() + 1

def findSmallest(a_list):
    answer = max(a_list) + 1
    for num in a_list:
        if num < answer:
            answer = num
    return answer

print(findSmallest([50,30,4,2,11,0])) # 0
print(findSmallest([40,3,4,2])) # 2

def find_smallest(l):
    l.sort()
    answer = l.pop(0)
    return answer

print(find_smallest([50,30,4,2,11,0])) # 0
print(find_smallest([40,3,4,2])) # 2