class Solution:
   def maximumGain(self,s: str, x: int, y: int) -> int:
      
      if x >= y:
         first, first_points, second, second_points = "ab", x, "ba", y
      else:
         first, first_points, second, second_points = "ba", y, "ab", x

      
      def remove_substrings(s: str, sub: str, points: int) -> (str, int):
         stack = []
         score = 0
         for char in s:
               if stack and stack[-1] == sub[0] and char == sub[1]:
                  stack.pop()
                  score += points
               else:
                  stack.append(char)
         return "".join(stack), score

      
      remaining_string, score = remove_substrings(s, first, first_points)
      
      remaining_string, score2 = remove_substrings(remaining_string, second, second_points)

      
      return score + score2

if __name__ == "__main__":
   sltn = Solution()
   s = "cdbcbbaaabab"
   x = 4
   y = 5
   sltn.maximumGain(s, x, y)
