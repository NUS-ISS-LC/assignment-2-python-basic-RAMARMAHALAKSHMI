def find(s, n):
# write your implementation here
    for i in range(0,len(s)-1):
        for j in range((i+1),len(s)):
            if s[i]+s[j]==n:
                return i,j
    return None

num=[3,2,4]
target=6
output=find(num, target)
print("Output: {}".format(output))