from pwdgenerator import Generator, Speed, Duration
from rich.table import Table
from rich.console import Console
from string import ascii_letters, digits, punctuation

console = Console()


def main():

    string = console.input(
        'Введите набор символов для генерации пароля или нажмите [cyan]Enter[/cyan]: ')
    string = string if len(
        string) >= 1 else ascii_letters + digits + punctuation
    console.print(f'Набор символов для генерации: [magenta]{string}[/magenta]')

    pwdgenerator = Generator(list(string))
    pwdgenerator.min_length = 6

    passwords = [

        # Вариант 1
        pwdgenerator.generate_by_params(
            P=10**(-4),
            V=Speed(15).aMinute,
            T=Duration(weeks=2),
        ),

        # Вариант 2
        pwdgenerator.generate_by_params(
            P=10**(-5),
            V=Speed(3).aMinute,
            T=Duration(days=10)
        ),

        # Вариант 3
        pwdgenerator.generate_by_params(
            P=10**(-6),
            V=Speed(10).aMinute,
            T=Duration(days=5)
        ),

        # Вариант 4
        pwdgenerator.generate_by_params(
            P=10**(-7),
            V=Speed(11).aMinute,
            T=Duration(days=6)
        ),

        # Вариант 5
        pwdgenerator.generate_by_params(
            P=10**(-4),
            V=Speed(100).aDay,
            T=Duration(days=12)
        ),

        # Вариант 6
        pwdgenerator.generate_by_params(
            P=10**(-5),
            V=Speed(10).aDay,
            T=Duration(days=30)
        ),

        # Вариант 7
        pwdgenerator.generate_by_params(
            P=10**(-6),
            V=Speed(20).aMinute,
            T=Duration(weeks=3)
        ),

        # Вариант 8
        pwdgenerator.generate_by_params(
            P=10**(-7),
            V=Speed(15).aMinute,
            T=Duration(days=20)
        ),

        # Вариант 9
        pwdgenerator.generate_by_params(
            P=10**(-4),
            V=Speed(3).aMinute,
            T=Duration(days=15)
        ),

        # Вариант 10
        pwdgenerator.generate_by_params(
            P=10**(-5),
            V=Speed(10).aMinute,
            T=Duration(weeks=1)
        ),

        # Вариант 11
        pwdgenerator.generate_by_params(
            P=10**(-6),
            V=Speed(11).aMinute,
            T=Duration(weeks=2)
        ),

        # Вариант 12
        pwdgenerator.generate_by_params(
            P=10**(-7),
            V=Speed(100).aDay,
            T=Duration(days=10)
        ),

        # Вариант 13
        pwdgenerator.generate_by_params(
            P=10**(-4),
            V=Speed(10).aDay,
            T=Duration(days=5)
        ),

        # Вариант 14
        pwdgenerator.generate_by_params(
            P=10**(-5),
            V=Speed(20).aMinute,
            T=Duration(days=6)
        ),

        # Вариант 15
        pwdgenerator.generate_by_params(
            P=10**(-6),
            V=Speed(15).aMinute,
            T=Duration(days=12)
        ),

        # Вариант 16
        pwdgenerator.generate_by_params(
            P=10**(-7),
            V=Speed(3).aMinute,
            T=Duration(days=30)
        ),

        # Вариант 17
        pwdgenerator.generate_by_params(
            P=10**(-4),
            V=Speed(10).aMinute,
            T=Duration(weeks=3)
        ),

        # Вариант 18
        pwdgenerator.generate_by_params(
            P=10**(-5),
            V=Speed(11).aMinute,
            T=Duration(days=20)
        ),

        # Вариант 19
        pwdgenerator.generate_by_params(
            P=10**(-6),
            V=Speed(100).aDay,
            T=Duration(days=15)
        ),

        # Вариант 20
        pwdgenerator.generate_by_params(
            P=10**(-7),
            V=Speed(10).aDay,
            T=Duration(weeks=1)
        ),

        # Вариант 21
        pwdgenerator.generate_by_params(
            P=10**(-4),
            V=Speed(20).aMinute,
            T=Duration(weeks=2)
        ),

        # Вариант 22
        pwdgenerator.generate_by_params(
            P=10**(-5),
            V=Speed(15).aMinute,
            T=Duration(days=10)
        ),

        # Вариант 23
        pwdgenerator.generate_by_params(
            P=10**(-6),
            V=Speed(3).aMinute,
            T=Duration(days=5)
        ),

        # Вариант 24
        pwdgenerator.generate_by_params(
            P=10**(-7),
            V=Speed(10).aMinute,
            T=Duration(days=6)
        ),

        # Вариант 25
        pwdgenerator.generate_by_params(
            P=10**(-4),
            V=Speed(11).aMinute,
            T=Duration(days=12)
        ),

        # Вариант 26
        pwdgenerator.generate_by_params(
            P=10**(-5),
            V=Speed(100).aDay,
            T=Duration(days=30)
        ),

        # Вариант 27
        pwdgenerator.generate_by_params(
            P=10**(-6),
            V=Speed(10).aDay,
            T=Duration(weeks=3)
        ),

        # Вариант 28
        pwdgenerator.generate_by_params(
            P=10**(-7),
            V=Speed(20).aMinute,
            T=Duration(days=20)
        ),

        # Вариант 29
        pwdgenerator.generate_by_params(
            P=10**(-4),
            V=Speed(15).aMinute,
            T=Duration(days=15)
        ),

        # Вариант 30
        pwdgenerator.generate_by_params(
            P=10**(-5),
            V=Speed(3).aMinute,
            T=Duration(weeks=1)
        )

    ]

    table = Table(show_header=True,
                  header_style='bold magenta', show_lines=True)

    table.add_column('Вариант')
    table.add_column('Пароль')
    table.add_column('A')
    table.add_column('L')
    table.add_column('P')
    table.add_column('V (паролей/день)')
    table.add_column('T (дней)')

    for i in range(len(passwords)):
        table.add_row(
            str(i + 1),
            str(passwords[i].password),
            str(passwords[i].A),
            str(passwords[i].L),
            str(passwords[i].P),
            str(passwords[i].V.inDays),
            str(passwords[i].T.inDays)
        )

    console.print(table)


if __name__ == '__main__':
    while(True):
        main()
        console.input('Продолжить...')
