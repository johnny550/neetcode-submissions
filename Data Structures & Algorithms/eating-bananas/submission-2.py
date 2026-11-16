class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r=1,max(piles)
        eating_rate=r

        
        while l<=r:
            potential_rate=(l+r)//2
            total_hours_taken=0
            for p in piles:
                # how many hours to eat all nanas POTENTIALLY
                hours_taken_per_pile=math.ceil(p/potential_rate)
                total_hours_taken+=hours_taken_per_pile
            
            
            if total_hours_taken<=h:
                # consider this a the new potential eating rate
                eating_rate=min(eating_rate,potential_rate)
                
                # eat slowly
                # decrease the hourly eating rate
                # look to the left
                r=potential_rate-1
            else:
                # eat faster
                # increase the hourly eating rate
                # look to the right
                l=potential_rate+1

        return eating_rate
