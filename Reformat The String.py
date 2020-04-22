class Solution:
    def reformat(self, s: str) -> str:
        num = "0123456789"
        c_num = 0
        c_alpha = 0
        n = ""
        al = ""
        for i in s:
            if i in num:
                c_num += 1
                n += i
            else:
                c_alpha += 1
                al += i
        #print(abs(c_num-c_alpha))
        if abs(c_num - c_alpha) > 1:
            return ""
        else:
            li = ""
            if c_num > c_alpha:
                for i in range(len(s)):
                    if i % 2 == 0:
                        li += n[i // 2]
                    else:
                        li += al[(i-1) // 2]
            else:
                for i in range(len(s)):
                    #print(li)
                    if i % 2 == 0:
                        li += al[i // 2]
                    else:
                        li += n[(i-1) // 2]
            return li
