def make_menu(title, **options):
    """
    Berilgan sarlavha va variantlar bilan menyu yaratadi.

    Args:
        title (str): Menyu sarlavhasi.
        **options (dict): Variantlar juftliklari, kalit (variant raqami) va qiymat (variant nomi).

    Returns:
        str: Yaratilgan menyu satrlar to'plami sifatida.
    """
    head = f'┏{f" {title} ".center(100, "━")}┓'
    for k, v in options.items():
        option = f'\n┃ {k}: {v}'
        head += option + ' ' * (102 - len(option)) + '┃'
    head += f"\n┗{'━' * 100}┛"
    return head
