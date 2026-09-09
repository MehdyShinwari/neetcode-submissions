class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l, r = 0, len(people)-1
        boats = 0
        while l < r:
            if people[r] % limit == 0:
                boats +=1
                r -= 1
            if (people[r] + people[l]) % limit == 0:
                boats +=1
                r -=1
                l +=1
        if l == r:
            boats +=1
        return boats