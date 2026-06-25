class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_s = ""
        for s in strs:
            slen = len(s)
            encoded_s += (str(slen) + "#" + s)
        print(encoded_s)
        return encoded_s



    def decode(self, s: str) -> List[str]:
        decoded_list = []

        slen = ""

        i = 0
        while i < len(s):
            if s[i] != "#":
                slen += s[i]
            elif s[i] == "#":
                slen_int = int(slen)
                slen = ""
                curr_s = ""

                j = 1
                while j <= slen_int:
                    curr_s += s[i + j]
                    j += 1
                    #print(curr_s, i, j)
                i += j
                decoded_list.append(curr_s)
                continue
            i += 1
        return decoded_list
            

        return 
