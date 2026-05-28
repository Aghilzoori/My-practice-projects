from config import QUESTION_LIST
from colorama import Fore
from core.printt import remove_text_from_trminal, edit_text
from core.core import main as ma
print('برای خروج کلمه پایان وارد کنید یا عدد 3')
print('سلام به ازمون هوش هاس جند گانه خوش امدین در این ازمون شما متوجه میشوید چه نوع شخصیت دارید از شما 30 سوال پرسیده میشود و شما تلاش میکنید تا به این سوال ها  با دقیق پاسخ بدهید زمان وجود ندارد پس لطفا وقت بزارید')

help_text = """
پاسخ سوال ها به شکل زیر هست 
مخالفم = 25
نظری ندارم = 50
موافقم = 75
کاملا موافقم = 100
شما میتوانید عدد که هست بگویید 
"""

print(Fore.RED + help_text, True)

print(Fore.GREEN)

print(QUESTION_LIST[0])

print('25 50 75 100')

@edit_text
def main(inputt):
    question = ma(inputt)
    if question[0] == 'BLUE':
        return 'BLUE', question[1] + '\n'
    return question[0], question[1] + '\n' + '25 50 75 100'

while True:
    try:
        inputt = input('-> ')
        if inputt == '3' or inputt == 'پایان':
            break
        main(int(inputt))
    except Exception:
        pass