class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list= list(s)
        t_list=list(t)
        s_charcount={}
        t_charcount={}
        ns=len(s_list)
        nt=len(t_list)

        for i in range(0,ns):
            if s_list[i] in s_charcount:
                s_charcount[s_list[i]]+=1
            else:
                s_charcount[s_list[i]]=1

        for i in range(0,nt):
            if t_list[i] in t_charcount:
                t_charcount[t_list[i]]+=1
            else:
                t_charcount[t_list[i]]=1
        if t_charcount == s_charcount:
            return True
        else:
            return False

            
