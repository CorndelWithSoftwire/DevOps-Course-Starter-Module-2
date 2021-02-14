from flask import session
from todo_app.data import trello as session


_DEFAULT_ITEMS = [
    { 'id': 1, 'status': 'Not Started', 'title': 'List saved todo items' },
    { 'id': 2, 'status': 'Not Started', 'title': 'Allow new items to be added' }
]


def get_items():
    """
    Fetches all saved items from the session.

    Returns:
        list: The list of saved items.
    """

    return session.get_cards_from_list()    
# https://api.trello.com/1/boards/602594185d55a18c4ea20b22?key=cb605ca676872005168aace21b9fbb90&token=2196313085b9d57c0cffee9e5b4e95326e4fa780b8273d8219461ac061f8a23f
# https://api.trello.com/1/lists/602594185d55a18c4ea20b23/cards?key=cb605ca676872005168aace21b9fbb90&token=2196313085b9d57c0cffee9e5b4e95326e4fa780b8273d8219461ac061f8a23f
# https://api.trello.com/1/lists/602594185d55a18c4ea20b23/cards?key=cb605ca676872005168aace21b9fbb90&token=2196313085b9d57c0cffee9e5b4e95326e4fa780b8273d8219461ac061f8a23f
    # return session.get('items', _DEFAULT_ITEMS)


def get_item(id):
    """
    Fetches the saved item with the specified ID.

    Args:
        id: The ID of the item.

    Returns:
        item: The saved item, or None if no items match the specified ID.
    """
    items = get_items()
    return next((item for item in items if item['id'] == int(id)), None)


def add_item(title):
    """
    Adds a new item with the specified title to the session.

    Args:
        title: The title of the item.

    Returns:
        item: The saved item.
    """
    items = get_items()

    # Determine the ID for the item based on that of the previously added item
    id = items[-1]['id'] + 1 if items else 0

    item = { 'id': id, 'title': title, 'status': 'Not Started' }

    # Add the item to the list
    items.append(item)
    session['items'] = items

    return item


def save_item(item):
    """
    Updates an existing item in the session. If no existing item matches the ID of the specified item, nothing is saved.

    Args:
        item: The item to save.
    """
    existing_items = get_items()
    updated_items = [item if item['id'] == existing_item['id'] else existing_item for existing_item in existing_items]

    session['items'] = updated_items

    return item


def complete_item(id):
    item = get_item(id)

    if item != None:
        item['status'] = 'Completed'
        save_item(item)

    return item
