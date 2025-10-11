# https://school.programmers.co.kr/learn/courses/30/lessons/42888
# 2019 카카오 블라인드 채용


def solution(record):
    answer = []
    uid_dict = {} # uid와 nickname의 관계를 저장하는 dictionary
    printer = {'Enter': '님이 들어왔습니다.', 'Leave': '님이 나갔습니다.'}
    
    for r in record:
        rr = r.split(' ')
        # 새로운 유저가 들어오거나, 기존 유저의 닉네임이 변경되는 경우 uid_dict 갱신
        if rr[0] in ['Enter', 'Change']:
            uid_dict[rr[1]] = rr[2]
    
    for r in record:
        rr = r.split(' ')
        # 최종 채팅방 메시지
        if rr[0] != 'Change':
            answer.append(uid_dict[rr[1]] + printer[rr[0]])
    
    return answer