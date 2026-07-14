class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ''
        for mot in strs:
            out+= f'{len(mot)})'
            out+= mot
        return out

    def decode(self, s: str) -> List[str]:
        out = []
        i = 0
        while i < len(s)-1:
            j = i
            while s[j]!=')':
                j+=1

            current_n = j-i #len du nombre auquel on a affaire
            current_nb = int(s[i:j])

            out.append(s[j+1:j+current_nb+1])

            i = j+current_nb+1

        return out


