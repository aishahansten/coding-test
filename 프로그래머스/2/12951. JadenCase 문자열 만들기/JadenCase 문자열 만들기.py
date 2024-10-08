def solution(s):
    answer = ''
    s_list = s.split(' ')
    ans_list = []
    
    for i in s_list:
        ans_list.append(i.capitalize())
    answer = ' '.join(ans_list)
                
    return answer