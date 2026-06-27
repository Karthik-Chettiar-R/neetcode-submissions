class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs2=[]
        done=[0]*len(strs)

        ret=[]
        
        for i in range(len(strs)):
            strs2.append(''.join(sorted(strs[i])))
        
        for i in range(len(strs)):
            listtemp=[]
            for j in range(i+1,len(strs)):
                if not done[i] and (strs2[i]==strs2[j]):
                    done[j]=1
                    listtemp.append(strs[j])
            if(not done[i]):
                listtemp.append(strs[i])
                done[i]=1
            if len(listtemp)!=0:
                ret.append(listtemp)


        return ret
    
        
        
  
       