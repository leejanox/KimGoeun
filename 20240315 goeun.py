# #import math 미리 만들어진 것을 불러오는 것(수학)
# #int 정수형 float 실수형 none 없다 bool (0 거짓 1 참) bool(문자형)=참

# import math
# a=int(3.5)
# print(a)

# # 필요할떄마다 다른 라이브러리 불러오기
# # 식별자 쓰기
# # 기본적 규칙 1.들여쓰기, 띄어쓰기 하기(줄 바꿔가며 쓰기)
# # 텍스트 문자열 strings: 'cat' 따옴표 붙이기
# # 여러줄 주석처리 1.드래그 후 컨트롤+슬래시 
# # 사칙연산 +,-,*,/,제곱(**), 나머지 산출 (%), 나누기 후 소수점 버리기 (//)

# #5+2 치면 바로 결과 x 변수 정하고 프린트까지.

# #비교연산자(관계연산자) 등호(==), 같지 않음(!=), 부등호(<,>,<=,>=)

# a=2
# if a != 1:  #이 줄이 진짜 일때만 터미널에 답이 나옴.
#     print("1이 아님")

# a=1
# if a == 1:
#     print("1이 아님")

# a=0
# if a <= 1:
#     print("1이 아님") #if 일때 문장 끊어주려고 : 을 쓴다.

# a=2
# if a >= 1:
#     print("1이 아님")

# #할당 연산자 :변수에 값을 할당하기 위해 사용, 시본적으로 = 을 사용한다
# #다른 산술연산자도 간결히 표현하기 위해 /=, +=,-=,*=,%= 이렇게 쓴다.
# #a= a*10 이랑 a*= 10 이랑 같다.
    
# #논리연산자:and (양 쪽 값이 다 참 일 때), or( 한 쪽 값만 참 일 때), not(양 쪽 값이 다 거짓 일 때)
# # if 줄은':'로 끊어 주고 거짓일때 나오는 답은 else: 로 나오게 쓴다 

# #멤버쉽 연산자 [] : 리스트 라고 부름
# #좌측 Operand가 우측에 속해 있는지 아닌지 체크

# #in, not in 이 있다. 양쪽이 참인지 아닌지 판단하는 것  

# a="ABC"
# b=a
# print(a is b) #참

# # 문자열 s='가나다' , s="가나다" 다 똑같음 , 여러줄 문자열 표현은 앞 뒤에 ''' 세개씩 붙인다.

# s= '아리랑'
# s= "아리랑"

# s= '''아리랑
# 아리랑
# 아리랑
# 아라리오'''

# s= '아리랑\n아리랑\n아라리오\n입니다'
# print(s)

# #문자열 포맷팅 : 대입값이 들어갈 자리를 지정해 두고 나중에 값을 채워넣는 방식
# # '%s' :문자열이 들어감 '%d' : 숫자가 들어감 f(소수점 나타냄, 3f = 소수점 3자리를 보여준다 는 뜻)

# #문자열 = str라는 클래스 타입, 한 번 설정되면 변경 시킬수 없다

# s="ABC"
# type(s) #s의 타입이 뭐냐
# V= s[1] #프로그램은 0부터 시작 따라서 1은 2번째 (문자열은 인덱스를 사용하여 문자열 중 특정위치의 문자를 표현 할 수 있다, 인덱스는 0으로부터시작한다. )
# type(s[1]) #s[1]이 어떤 클래스냐 = 문자열 

# #파일을 가져올때는 r'파일주소' 
# # path = r 'C:~~~~'
# # print(path)

# #여러 개의 문자열을 붙여서 표현하고 싶을때는 join을 쓴다.

# s= ','.join(['가나','다라','마바']) #쉼표를 빼고 가지고 올 때는 ','를 ''로 하면 된다.
# print(s) # 출력:가나 , 다라 , 마바

# #쪼갤 때는 .split(',') =쉼표 넣고 쪼개기 문자열 뒤에쓴다

# #ppt75장 다시 물어보기...
# #ppt76장 3번째 왜 x..?

# #분류할때 ; 사용하기도 함

# #if 구문은 4칸 (탭) 들여쓰기를 꼭 해야함.
# a=10
# if a== 10:
#     print('10입니다.')

# a=10
# if a== 10:
#     print('10')
#     print('입니다')# 이렇게 쓸때는 print줄 위치를 맞춰준다.

# x = 10
# if x < 10:
#     print(x)
#     print('한자리수')

# if x < 100:
#     print(x)

# #if 거짓일때 다음 elif(else if)로 넘어감 그 다음 모든 if문이 거짓일때는 else: 를 실행 할 수 있다.
    
# x=10
# if x < 10:
#     print("한자리수")
# elif x < 100:
#     print("두자리수")
# else:
#     print("세자리수")

# #if 조건문 안에서 특정 문장을 수행하지 않고 스킵하기 위해 pass 라는 키워드를 사용

# n=7
# if n < 10:
#     pass
# else:
#     print(n)

# #인풋 함수=input() : 변수를 만들 떄 값을 직접 할당해주면 고정된 값만 사용 가능. 따라서 매번 다른 값을 변수에 할당하려면 input함수를 사용한다.

# x=input('문자열을 입력하세요:')
# print(x)

# y=input('당신의 이름은 무엇입니까?:')
# print(y)

# #반복문 While 키워드 다음의 조건식이 참일 경우 계정 while안의 블럭을 실행.

# i=1
# while i <= 10: #참. 다음줄로 넘어감
#     print(i)
#     i+=1 # i=i+1

# #반복문 for.
    
# sum=0
# for i in range(11): #0~10
#     sum += i #sum= sum+i
# print(sum) #0부터 10까지 더하는 코드 

# list=["this","is","a","book"]
# for s in list:
#     print(s)

#반복문. 루프를 빠져나오기 위해 break문을 사용 할 수 있다. continue는 루프 블럭 나머지 문장 실행 x 다음 루프로 돌아가게 할 수 있다.

# i=0
# sum=0
# while True:
#     i+=1
#     if i==5:
#         continue
#     if i > 10:
#         break
#     sum +=i

# print(sum)  답은 50

#반복문 range() , 1~3개의 파라미터를 가짐, 파라미터는 파라미터 갯수에 따라 다른 의미를 가진다.

number = range(2,11,2)

for x in numbers:
    print(x)
