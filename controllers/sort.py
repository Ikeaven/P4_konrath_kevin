""" Thie module sort lists """


from views.utilities import UtilitiesView


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
        sorted_list = sorted(players, key=lambda x: x.first_name.lower(), reverse=False)
        sorted_list = sorted(sorted_list, key=lambda x: x.last_name.lower(), reverse=False)
    else:
        UtilitiesView().display_error_with_message('Erreur: Valeur non trouvé')
        return None
    return sorted_list
