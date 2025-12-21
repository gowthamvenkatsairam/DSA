class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        n = len(s)
        result, path = [], []
        def possibleStrings(idx):
            if idx == n:
                result.append("".join(path))
                return
            ch = s[idx]
            if ch.isdigit():
                path.append(ch)
                possibleStrings(idx + 1)
                path.pop()
            else:
                path.append(ch)
                possibleStrings(idx + 1)
                path.pop()
                path.append(ch.lower() if ch.isupper() else ch.upper())
                possibleStrings(idx + 1)
                path.pop()
        possibleStrings(0)
        return result
                
            
            

            
            


