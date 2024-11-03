p=["The quick brown fox jumps over the lazy dog."]
print(p)

# How do you slice the paragraph to get the first 10 characters?
print(p[0][0:10])

#How do you slice the paragraph to get the last 10 characters?
print(p[0][-10:])

#How do you slice the paragraph to get every other character?
print(p[0][0::2])

#How do you slice the paragraph to get the characters in reverse order?
print(p[0][:0:-1])

#How do you slice the paragraph to get the words "quick brown"?
print(p[0][4:15:1])

#How do you slice the paragraph to get the words "lazy dog"?
print(p[0][-9:-1:1])

#How do you slice the paragraph to get the characters from index 10 to 20?
print(p[0][10:21])

#How do you slice the paragraph to get the characters from index 5 to 15?
print(p[0][5:16])

#How do you slice the paragraph to get the characters from the end of the paragraph to index 20?
print(p[0][-1:20:-1])

#How do you slice the paragraph to get the characters from index 15 to the end of the paragraph
print(p[0][15::1])