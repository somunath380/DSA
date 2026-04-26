
def reverseWords(s):
    ans = ""
    for word in s.split(' '):
        ans += word[::-1] + " "
    return ans[:len(ans)-1:]

s = "Let's take LeetCode contest"
#"s'teL ekat edoCteeL tsetnoc"
print(reverseWords(s))