class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start, end = 0 , 0
        max_frq, wnd_size = 0, 0
        freq = {}
        max_l = 0
        for end, ch in enumerate(s):
            '''if end in chars:
                chars[end] += 1 #while creating dict only create no pther options
            chars[end] = 1'''
            freq[ch] = freq.get(ch,0) + 1
            max_frq = max(max_frq, freq[ch])
            wnd_size = end - start + 1
            if wnd_size - max_frq > k:
                freq[s[start]] -= 1
                start += 1
            current_l = end - start + 1
            max_l = max(max_l, current_l)
        return max_l

            
        

            
        