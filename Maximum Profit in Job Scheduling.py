class Solution(object):
    def jobScheduling(self, startTime, endTime, profit):
        ends = []
        countProfit = 0
        for start, end, economizedTime in sorted(zip(startTime, endTime, profit)):
            while ends and ends[0][0] <= start:
                countProfit = max(countProfit, heappop(ends)[1])
                
            countedAndEconomized=countProfit+economizedTime
            heappush(ends, (end, countedAndEconomized))
            maxGainedTime=max(x[1] for x in ends)
            
        return maxGainedTime
