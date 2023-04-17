import urwid


def has_digit(password):
    return any(char.isdigit() for char in password)


def is_very_long(password):
    return len(password) >= 12


def has_letters(password):
    return any(char.isalpha() for char in password)


def has_upper_letters(password):
    return any(char.isupper() for char in password)


def has_lower_letters(password):
    return any(char.islower() for char in password)


def has_symbols(password):
    return not all(char.isalpha() or char.isdigit() for char in password)


def get_password_score(password):
    checks = [
        has_digit,
        is_very_long,
        has_letters,
        has_upper_letters,
        has_lower_letters,
        has_symbols
    ]

    score = sum(2 for check in checks if check(password))
    return score


def on_ask_change(edit, new_edit_text, reply_text):
    score = get_password_score(new_edit_text)
    reply_text.set_text("Password rating: %s" % score)


def create_menu():
    ask = urwid.Edit('Insert password: ', mask='*')
    reply_text = urwid.Text("")
    urwid.connect_signal(ask, 'change', on_ask_change, reply_text)
    menu = urwid.Pile([ask, reply_text])
    menu = urwid.Filler(menu, valign='top')
    loop = urwid.MainLoop(menu)
    loop.run()


def main():
    create_menu()


if __name__ == '__main__':
    main()






