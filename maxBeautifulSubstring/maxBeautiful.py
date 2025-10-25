class Solution:
    def maximizeBeautifulSubstrings(self, color: str) -> int:
      s = list(color)
      n = len(color)

      for i in range(n):
        if s[i] == '.':
          if i > 0 and s[i - 1] != '.':
            s[i] = s[i - 1]
          else:
            j = i + 1
            while j < n and s[j] == '.':
              j+=1
            s[i] = s[j] if j < n else 'a'
      
      total = 0
      count = 1
      for i in range(1, n):
        if s[i] == s[i-1]:
          count += 1
        else:
          total += count * (count + 1) // 2
          count = 1
      total += count * (count + 1) // 2

      return total
