class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack=[]
        stack.append(0)

        warmerDays=[0 for i in range(len(temperatures))]

        for i in range(1,len(temperatures)):
            if temperatures[i]>temperatures[stack[-1]]:
                while(stack and temperatures[stack[-1]]<temperatures[i]):
                    day=stack.pop()
                    warmerDays[day]=i-day
            stack.append(i)
        


        if stack:
            for i in stack:
                warmerDays[i]=0

        return warmerDays

    
        