""" Thie module sort lists """


def sort_list_by(players, tri):
    """Sort the list of players by ranking or alphabetical order.

    Args:
        players ([Players list]): List of players instances
        tri (str): must be 'ranking' or 'last_name'

    Returns:
        [Players list]: sorted list of players instances
    """
    if tri == '1':
        sorted_list = sorted(players, key=lambda x: x.ranking, reverse=True)
    elif tri == '2':
        sorted_list = sorted(players, key=lambda x: x.last_name, reverse=False)
    return sorted_list
