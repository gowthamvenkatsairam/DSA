class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        dp = {}
        def findminCost(req):
            req_tuple = tuple(req)
            if req_tuple in dp:
                return dp[req_tuple]
            min_cost = sum(req[i] * price[i] for i in range(len(req)))
            for offer in special:
                valid = True
                temp = []
                for j in range(len(req)):
                    if offer[j] > req[j]:
                        valid = False
                        break
                    temp.append(req[j] - offer[j])
                if valid:
                    cost_with_offer = offer[-1] + findminCost(temp)
                    min_cost = min(min_cost, cost_with_offer)
            dp[req_tuple] = min_cost
            return min_cost
        return findminCost(needs)
            




