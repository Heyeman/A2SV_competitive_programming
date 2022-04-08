class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left = n = 0
        l = len(people) -1    
        while people:
            rem = people.pop()
            if people and rem + people[left] <= limit:
                people.pop(left)
            n +=1

        return n
         
