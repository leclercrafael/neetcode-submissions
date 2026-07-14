from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1)>len(s2):
            return False

        else:
            
            target = Counter(s1)
            current = Counter(s2[:len(s1)])

            if current == target:
                return True

            for i in range(len(s2)-len(s1)):
                current[s2[i]] -=1
                current[s2[i+len(s1)]] = current.get(s2[i+len(s1)],0) +1
                if current[s2[i]] == 0:
                    del current[s2[i]]
                if current == target:
                    return True
                
                

        return False
