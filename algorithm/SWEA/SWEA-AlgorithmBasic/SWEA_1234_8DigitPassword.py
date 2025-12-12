def isPassword(word):
    stack = []
    for w in word:
        stack.append(w)
        if len(stack) < 2:
            pass
        elif len(stack) >= 2:
            if stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()
                
    # return ''.join(word)
    # word는 원래의 문자열, stack을 이용해 새로운 문자열
    
    # ''.join(): 공백없이 리스트를 하나의 문자열로 만들기
    return ''.join(stack)

# # 줄여서 쓰기
# def isPassword(word):
#     stack = []
#     for w in word:
#         stack.append(w)
#         if len(stack) >= 2 and stack[-1] == stack[-2]:
#             stack.pop()
#             stack.pop()
    
#     return ''.join(stack)

# # 변수명 변경
# def remove_adjacent_duplicates(digits):
#     stack = []
#     for digit in digits:
#         stack.append(digit)
#         if len(stack) >= 2 and stack[-1] == stack[-2]:
#             stack.pop()
#             stack.pop()
                
#     return ''.join(stack)

T = 10
for t in range(1, T+1):
    N, string = input().split()
    password = isPassword(string)
    print(f'#{t} {password}')