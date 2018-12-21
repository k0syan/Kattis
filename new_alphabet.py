original = list("abcdefghijklmnopqrstuvwxyz")
new = ["@", "8", "(", "|)", "3", "#", "6", "[-]", "|", "_|", "|<", "1", "[]\/[]", "[]\[]", "0", "|D", "(,)", "|Z", "$",
       "']['", "|_|", "\/", "\/\/", "}{", "`/", "2"]
string = input().lower()
new_string = ""
for i in range(len(string)):
    chars = list(string)
    if chars[i] in original:
        new_string += new[original.index(chars[i])]
    else:
        new_string += chars[i]
print(new_string)
