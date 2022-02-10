class Solution:
    def trans(self,st):
        ans=""
        st=st.split()
        st.reverse()
        print(st)


        return ' '.join(st)
st="  hello world!  "
s=Solution()
print(s.trans(st))