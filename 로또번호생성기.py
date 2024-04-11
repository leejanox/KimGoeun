import random
lotto=input("로또 번호 생성기! 번호를 뽑으시려면 Y, 아니라면 N을 입력해주세요 : \n")
if lotto.upper()=="Y":
    random_number= random.sample(range(1,46),6)
    print(f"이번주 로또 번호는 {random_number} 입니다.")
else:
    print("안녕히가세요.")