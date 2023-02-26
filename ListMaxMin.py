numbers = []
for n in input('숫자를 여러개 입력해주세요. :').split():
    numbers.append(int(n))
 
print(numbers) #리스트 출력
max_value = max(numbers)
min_value = min(numbers)
print(f'가장 큰 값 : {max_value}')
print(f'가장 작은 값 : {min_value}')
 
numbers.remove(max_value)
numbers.remove(min_value)
average = sum(numbers)/len(numbers) #리스트 값의 평균
 
print(f'나머지 값의 평균 : {average}')