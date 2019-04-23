if __name__ == "__main__":
    n = int(input())
    chars = list(input())
    final_list = []
    for i in range(len(chars)):
        char = chars[i]
        if char != " ":
            if len(final_list) == 0:
                final_list.append(char)
            else:
                if char == "[" or char == "{" or char == "(":
                    final_list.append(char)
                else:
                    if char == "]":
                        if final_list[len(final_list) - 1] != "[":
                            print(char, i)
                            break
                        elif len(final_list) == 0:
                            print(char, i)
                            break
                        else:
                            del final_list[-1]
                    elif char == "}":
                        if final_list[len(final_list) - 1] != "{":
                            print(char, i)
                            break
                        elif len(final_list) == 0:
                            print(char, i)
                            break
                        else:
                            del final_list[-1]
                    elif char == ")":
                        if final_list[len(final_list) - 1] != "(":
                            print(char, i)
                            break
                        elif len(final_list) == 0:
                            print(char, i)
                            break
                        else:
                            del final_list[-1]
    if len(final_list) == 0:
        print("ok so far")
