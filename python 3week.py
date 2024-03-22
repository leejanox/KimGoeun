# # mystery=734_529.678 #_ 언더바는 소수점이랑 똑같이 씀. 따라서 실수.
# # print(type(mystery))

# #type() 함수를 써서 어떤 데이터 형식인지 확인해 볼 수 있다

# num_char=len(input("당신의 이름은 무엇입니까?"))
# print(type(num_char)) 
#len 은 길이를 구함 따라서 이름 김고은을 치면 num_char는 3이 되고 타입을 물어보면 int가 나옴.

# #문제:2자리의 숫자를 입력받아 앞자리와 뒷자리의 값을 더하세요.

# a=input("두자리 수를 입력하세요: ")
# print(a)

# # #입력값이 2자리인지 확인
# if len(a) !=2:
#    print("두자리 수를 입력하세요: ")
# #     #각 자리의 숫자를 추출하여 정수로 변환하여 더하기
# else:
#     first_A= int(a[0]) 
#    second_A=int(a[1])
#    result=first_A+second_A
#    print(result)


# #BMI계산기

# height=input("당신의 키는 몇 m 입니까?: ")
# weight=input("당신의 몸무게는 몇 kg 입니까?: ")

# bmi = int(weight)/float(height)**2
# bmi_as_int=int(bmi)
# print(bmi_as_int)

# score=0
# score+=1
# print(score)

## f-string
#score=0
#height=1.8
#earth=True
#print(type(score))
#print(type(height))
#print(type(earth))
#print(f"당신의 스코어는 {score},당신의 키는 {height}, 당신은 지구인 입니다.{earth}")