from colorama import Fore

def remove_text_from_trminal(line : int):
    print("\033[F\033[K" * line, end="")

def edit_text(func):
    def color_print(*args, **kwargs):
        color, result = func(*args, **kwargs)
        if color == 'RED':
            print(Fore.RED + result)
        elif color == 'GREEN':
            print(Fore.GREEN + result)
        elif color == 'BLUE':
            print(Fore.BLUE + result)
        else:
            print(result)
    return color_print