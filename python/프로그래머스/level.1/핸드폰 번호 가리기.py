def solution(phone_number):
    a = len(phone_number)
    return (a-4)*'*'+phone_number[-4:]
