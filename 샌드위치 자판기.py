#샌드위치 자판기

print("샌드위치를 드시러 오셨군요! \n")
bill=0 
size= input("사이즈를 선택 하세요 S,M,L : ") 

if size.upper() == "s": 
    bill=5000 
    print("S사이즈를 선택하셨습니다.")
elif size.upper() == "m":
    bill=7000 
    print("M사이즈를 선택하셨습니다.")
else:
    bill=10000 

bread=input("빵을 선택해 주세요! 종류는 위트, 화이트, 플랫브레드, 허니오트 총 네 가지 입니다. : ")
if bread == "위트":
    bill+=0
    print("위트를 선택하셨습니다. 추가금은 0원입니다.")
elif bread == "플랫브레드":
    bill+=500
    print("플랫브레드를 선택하셨습니다. 추가금은 500원입니다.")
elif bread == "화이트":
    bill+=0
    print("화이트를 선택하셨습니다. 추가금은 0원입니다.")
else:
    bill+=500
    print("허니오트를 선택하셨습니다. 추가금은 500원입니다.")

meat=input("고기 종류를 골라주세요. 종류는 베이컨, 에그마요, 페퍼로니, 새우 총 네 가지 입니다. : ")
if meat == "베이컨":
    bill+=500
    print("베이컨을 선택하셨습니다. 추가금은 500원입니다.")
elif meat == "에그마요":
    bill+=500
    print("에그마요를 선택하셨습니다. 추가금은 500원입니다.")
elif meat == "페퍼로니":
    bill+=300
    print("페퍼로니를 선택하셨습니다. 추가금은 300원입니다.")
else:
    bill+=800
    print("새우를 선택하셨습니다. 추가금은 800원입니다.")

sauce=input("소스를 뿌리시겠습니까? yes(y) or no(n) or 추가(+500원) : ")
if sauce.upper() == "y":
    bill+=0
elif sauce.upper() == "n":
    bill+=0
else:
    bill+=500
    print(f"총 지불하실 금액은 {int(bill)}원 입니다. 학생이시면 10% 할인을 받을 수 있습니다!")

std=input("학생 할인을 받으시겠습니까? yes(y) or no(n) : ")
if std.lower() == "y":
    bill *=0.9 
    print(f"10%할인되셨습니다! 총 지불하실 금액은 {int(bill)}원 입니다!")
else:
    bill
    print(f"할인을 받지 않으셨습니다. 총 지불하실 금액은 {int(bill)}원 입니다!")