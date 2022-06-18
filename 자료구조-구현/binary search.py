# 구현을 위한 준비
# target : 찾고자 하는 값
# data : 오름차순으로 정렬된 list
# start : data 의 처음 값 인덱스
# end : data 의 마지막 값 인덱스
# mid : start, end 의 중간 인덱스

# 구현 개요
# 자료의 중간 값이 (mid) 찾고자 하는 값인지 검사
# 아니라면 대소관계를 비교하여 start, end 값 이동
# 동일 연산 반복 (재귀로 구현 가능)

def binary_search(target, data):
    data.sort()
    start = 0
    end = len(data)-1

    while start <= end:
        mid = (start + end) // 2
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            start = mid + 1
        elif data[mid] > target:
            end = mid - 1
    return None


def binary_search_recursion(target, start, end, data):
    if start > end:
        return None

    mid = (start + end) // 2

    if data[mid] == target:
        return mid
    elif data[mid] < target:
        start = mid - 1
    elif data[mid] > target:
        start = mid + 1
    return binary_search_recursion(target, start, end, data)
