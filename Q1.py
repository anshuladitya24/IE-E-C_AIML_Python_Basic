# 1) Design an algorithm that counts the number of characters in a string without using len()
def charCountWithoutUsingLen(strn):
    count=0
    for i in strn:
        count = count+1

    return count

#sample
a = "hello"
print(charCountWithoutUsingLen(a))
