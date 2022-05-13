#파이썬 기본 문법
"""days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
 print(days) 결과 : ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'] / 배열 안 있는 그대로 출력
 print(days[3])  결과 : Thu / 배열과 유사
 print(len(days)) 결과 : 5 / 배열 안 들어있는 수
 days.append("Sat") 결과 : ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'] / 배열에 추가 """

""" sequence type 2 - tuple
common operation만 가능 (immutable)
아무도 변경할 수 없는 시퀀스를 만들고 싶을 때
()로 감싸서 만든다.

- Dictionary
{}로 만든다.
nico = {
"name": "Nico",
"age": 29,
"Korean": True,
"fav_food": ["Kimchi", "Sashimi"]
}

print(nico["name"])

-> dictionary 안에 정보를 list, tuple, boolean, number 등 다양한 type으로 저장할 수 있음"""

# 여러가지 선언 법

"""variable 선언 방법

변수명 = 값

※ 값을 넣을 때 string은 무조건 ""(큰따옴표)로 묶거나 ''(작은따옴표)로 묶어야한다. "' '" ← 이런식으로 큰따옴표랑 작은따옴표를 섞어쓰면 안 된다!! ※
※ 값의 첫 글자는 대문자로 써줘야 한다. ex) a = True / b = False / c = None (문자열같이 따옴표로 묶인 것들은 제외) ※
※ 변수 타입을 알고싶으면 print(type(변수명))으로 알아볼 수 있다. ※


이름 표기 방법
Python에서는 snake case 사용. (뱀 같다 하여 snake case라 함.)
이름을 지을 때 소문자를 사용하며 단어를 분리할 때 띄어쓰기 대신 _를 쓴다 ex) super_long_variable

타 프로그래밍 언어에서는 camel case 사용. (낙타의 등과 닮았다하여 camel case라 함.)
소문자로 시작하되 단어를 분리할 때 공백없이 첫글자를 대문자로 시작한다. ex) superLongVariable

※ 꼭 이 규칙을 지키지 않더라도 작동은 하나, 코드를 통일성 있게 보기위한 하나의 약속임. ※

--

sequence type : list / tuple

list 선언 방법

리스트명 = [값, 값, ...]

※ 대괄호 안에 값을 넣어주며 ,로 값을 구분함 ※
※ index는 0부터 시작함! ※
※ list 생성 후 값을 추가, 삭제, 반전 등 다양하게 지지고 볶을 수 있음 (즉, list는 mutable함) ※

--

tuple 선언 방법

튜플명 = (값, 값, ...)

※ 소괄호 안에 값을 넣어주며 ,로 값을 구분함 ※
※ list와는 다르게 common sequence operation만 사용 가능함. (list는 Common and Mutable sequence operations 두 가지 모두 가능)
※ tuple 생성 후 마음대로 지지고 볶을 수 없으므로 아무도 변경할 수 없는 리스트를 만들고싶을 때 tuple을 사용함. (즉, tuple은 immutable함) ※


dictionary 선언 방법

딕셔너리명 = {"단어1" : 뜻, "단어2" : 뜻, ...}

※ 중괄호 안에 값을 넣어주며 단어는 큰따옴표로 묶고 콜론을 쓴 뒤 값을 넣어준다. 여러 단어를 정의할 때는 ,로 구분한다. ex) 좋아하는_음식 = {"음식" : "떡볶이", "가격" : 3000, "특징" : "맛있음"} ※
※ object를 만들 때 사용 ※
※ 특정 단어만 가져오길 원할 때 : 딕셔너리명["단어"] 로 끄집어낼 수 있음 ※
※ 생성 후 수정할 수 있음. ex) 딕셔너리명["단어"] = 값 으로 값을 추가할 수 있음 ※

※ 어떤 타입이든 dictionary, list, tuple안에 저장할 수 있음 ※

--

function : 어떤 행동(기능)을 가지고 있으며, 계속 반복 할 수 있음

※ print(), int()등 이런 함수들을 바로 쓸 수 있는 것은 built-in function이라 바로 쓸 수 있다. ※
※ 함수를 직접 정의해서 사용할 수 있다. ※

--
Python Standard Library에서 Python에 대한 정보를 확인할 수 있음."""

# 사용자 정의 함수 만들기 def

"""함수는 만든다고 부르기 보단 정의한다고 생각하면 편하다.
그래서 함수를 정의할 때에는 def(define의 약자)로 시작한다.
함수를 정의할 때는 들여쓰기(tab키를 눌러 들여쓰기할 수 있다)를 해야 함수내 기능들이
정상적으로 작동한다 *초보자들이 자주 하는 실수*

함수를 정의한 후 함수를 실행하기 위해서는 함수 이름 뒤에 '()'를 꼭 붙여야 실행된다.
*쉽게 생각해 함수를 작동시키는 버튼이라고 보면 된다* """

# 함수 정의

"""함수(funtion) 정의 시 def example(a,b) ==> a, b는 매개변수
호출 시 example(1,2) ==> 1,2는 인수(argument) ?

ex) def say_hello(who)
print("hello", who)

출력 시 - say_hello("jerri") ===> "hello jerri"

위의 who 자리에는 유효한(valid) 타입이라면 뭐든 넣을 수 있음. ex) boolean, number...
= function(함수)에 input(=data)를 주는 것.

덧셈 뺄셈의 경우

def plus(a, b) : def minus(a,b)
print(a + b) print(a - b)

출력 시 ===> plus(2, 5) minus(2, 5)

여기서 인수를 하나만 넣을 시 에러가 뜰 수 있음.
하지만 *default value를 입력하면 인수를 하나만 넣어도 함수가 성립.

ex) def plus(a, b=0):
print(a + b)

plus(2) ====> 출력 시 값 2가 나옴. (2 + 0)

마찬가지로 string 또한

def say_hello(name="anoymous"):
print("hello", name)
출력시 ====> say_hello() ----> hello anonymous
say_hello("nico") ----> hello nico """

# if else and or

"""if문이 true일 경우 해당 바디가 실행

false일 경우, 다음 elif.

false일 경우, 다음 elif

모두 false이므로 else



def age_checking(age):

print(f"you are {age}")

if age < 18:

print("you cant drink")

elif age == 18 or age == 19:

print("you new to this")

elif age > 20 or age < 25:

print("you are still kind of young")

else:

print("enjoy your drink")



age_checking(20) """

