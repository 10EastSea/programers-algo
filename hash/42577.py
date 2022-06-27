# 전화번호 목록
def solution(phone_book):
    answer = True

    phone_book_dict = {}
    for phone_num in phone_book:
        tmp = phone_book_dict
        for num in phone_num:
            check = tmp.get(num)
            if check is None:
                tmp[num] = {}
                tmp = tmp[num]
            else:
                check_fin = check.get("finish")
                if check_fin is None: tmp = check
                else: answer = False; break
        if len(tmp.keys()) > 0: answer = False
        
        if not answer: break
        tmp["finish"] = True

    # print(phone_book_dict)
    return answer