import sys

from colorama import init, Fore
from requests import Session

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.17 Safari/537.36",
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding': 'gzip,deflate',
    'Accept-Language': 'en-US,en;q=0.8',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive'
}
REQ_S = Session()
REQ_S.headers.update(headers)

init(autoreset=True)
fx = Fore.RESET
fc = Fore.CYAN
fg = Fore.GREEN
fw = Fore.WHITE
fr = Fore.RED
fb = Fore.BLUE
fy = Fore.YELLOW


def parse_arg() -> str:
    if len(sys.argv) > 1:
        return sys.argv[1]
    return ask('Enter domain:')


def clear():
    import os
    if 'win' in sys.platform.lower():
        os.system('cls')
    else:
        os.system('clear')


def pr(text: str, notation: str = '+'):
    x = fg
    if notation == '#':
        x = fc
    elif notation == 'X':
        x = fr
    elif notation == '!':
        x = fy
    elif notation == '?':
        x = fb

    print(f'{x}[{notation}]{fx} ' + text)


def choose(options: iter = ('Yes', 'No'), prompt: str = 'Choose action:', default: int = -1) -> int:
    if not options:
        raise ValueError(" [!] No options passed to choice() !!!")  # No options
    pr(prompt, '?')
    for index, option in enumerate(options):
        line = '\t'
        if index == default:
            line += '[%d]. ' % (index + 1)
        else:
            line += ' %d.  ' % (index + 1)
        line += option
        print(fy + line + fx)
    try:
        ans = input(fy + '[>>>] ' + fx)
        if not ans:
            return default
        ans = int(ans)
        assert 0 < ans <= len(options)
        return ans - 1
    except KeyboardInterrupt:
        return -2  # Keyboard Interrupt
    except AssertionError:
        return -1  # Bad Number
    except ValueError:
        return -1  # Probably text received


def ask(question: str) -> (None, str):
    pr(question, '?')
    answer = input('>')
    if answer == '':
        return None
    try:
        answer = int(answer)
    except ValueError:
        pass
    return answer


def pause(reason: str, cancel: bool = False):
    s = f'Press {fc}[ENTER]{fx} to ' + reason
    if cancel:
        s += ', %s to cancel' % fr + '[^C]' + fx
    pr(s, '?')

    try:
        input()
        return True
    except KeyboardInterrupt:
        return False
