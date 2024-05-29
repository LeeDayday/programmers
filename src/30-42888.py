# https://school.programmers.co.kr/learn/courses/30/lessons/42888
# 2019 카카오 블라인드 채용


def solution(record):
    answer = []
    uid_dict = {} # uid와 nickname의 관계를 저장하는 dictionary
    for i in range(len(record)):
        tmp_record = record[i].split(" ")
        # uid_dict에 uid가 존재하지 않는 경우, 추가
        if tmp_record[1] not in uid_dict:
            uid_dict[tmp_record[1]] = tmp_record[2]
        # nickname이 변경된 경우, 업데이트 하기
        if tmp_record[0] != 'Leave':
            if tmp_record[1] in uid_dict:
                if tmp_record[2] != uid_dict[tmp_record[1]]:
                    uid_dict[tmp_record[1]] = tmp_record[2]
    
    # answer에 들어갈 내용 만들기
    for i in range(len(record)):
        tmp_record = record[i].split(" ")
        nickname = uid_dict[tmp_record[1]]

        if tmp_record[0] == 'Enter':
            answer.append(f"{nickname}님이 들어왔습니다.")
        elif tmp_record[0] == 'Leave':
            answer.append(f"{nickname}님이 나갔습니다.")
    
    return answer


