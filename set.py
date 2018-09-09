char_list = ['a','a','b','b','c','c','c','d','d','d']
print(set(char_list))#删掉重复的部分，只保留不同的部分
print(type(set(char_list)))#类型是set


s = "Welcom back to this tutorial"
print(set(s))

unique_char = set(char_list)
unique_char.add('v')
print(unique_char)
