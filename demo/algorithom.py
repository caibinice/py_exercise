from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        if len(people) < 1 or people[len(people) - 1] > limit:
            return 0
        left, right, count = 0, len(people) - 1, 0
        while left <= right:
            sum = people[left]
            if left != right:
                sum += people[right]
            if sum > limit:
                right -= 1
            else:
                left += 1
                right -= 1
            count += 1
        return count
