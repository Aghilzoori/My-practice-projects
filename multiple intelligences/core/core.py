from config import QUESTION_LIST, help as HELP_DICT
from . import analyzer

user_answers: list[int] = []        
num_remaining_questions: int = 0    


def next_question() -> str:
    try:
        return QUESTION_LIST[num_remaining_questions]
    except Exception:
        return 'سوال ها تمام شد. 25 وارد کنید'

def separate_by_dimensions() -> dict[str, list[int]]:
    return {
        'analytic':   [user_answers[i] for i in [0, 6, 12, 18, 24]],
        'creative':   [user_answers[i] for i in [1, 7, 13, 19, 25]],
        'practical':  [user_answers[i] for i in [2, 8, 14, 20, 26]],
        'social':     [user_answers[i] for i in [3, 9, 15, 21, 27]],
        'introvert':  [user_answers[i] for i in [4, 10, 16, 22, 28]],
        'naturalist': [user_answers[i] for i in [5, 11, 17, 23, 29]],
    }


def generate_report_from_result(result_dict: dict) -> str:
    dominant = result_dict['dominant']
    percentages = result_dict['percentages']
    report = f"نوع ذهن غالب شما: {', '.join(dominant)}\n"
    for dim, p in percentages.items():
        report += f"{dim}: {p:.1f}%\n"
    return report


def character_traits(person: list[str]) -> str:
    key = person[0]          
    traits = HELP_DICT.get(key, [])
    return '\n'.join(traits)


def main(input: int) -> tuple[str, str]:

    global num_remaining_questions

    if num_remaining_questions == 30:
        dims = separate_by_dimensions()
        scores = analyzer.calculate_scores(
            dims['analytic'],
            dims['creative'],
            dims['practical'],
            dims['social'],
            dims['introvert'],
            dims['naturalist'],
        )
        dominant, max_val = analyzer.find_dominant_type(scores)
        percent = analyzer.normalize_scores(scores)

        result_of_test = {
            'dominant': dominant,
            'max_score': max_val,
            'percentages': percent,
            'raw_scores': scores,
        }

        report = generate_report_from_result(result_of_test)
        traits_info = character_traits(dominant)

        return ('BLUE', f"{report}\nویژگی هایی که دارند:\n{traits_info}")

    if input not in {25, 50, 75, 100}:
        return ('RED', "پاسخ صحیح نمی‌باشد")

    user_answers.append(input)
    num_remaining_questions += 1
    question = next_question()
    return ('GREEN', question)