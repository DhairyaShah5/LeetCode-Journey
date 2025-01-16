class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        boatCounter = 0

        left, right = 0, len(people) - 1

        while left <= right:
            remainingWeight = limit - people[right]
            right -= 1
            boatCounter += 1

            if left <= right and remainingWeight >= people[left]:
                left += 1

        return boatCounter