def get_todos():
    """
    this functions read todos.txt files content
    and then return a list of  todos.
    :return: list of todos
    """
    with open('todos.txt', 'r') as file:
        todos = file.readlines()
    return todos


def set_todos(todos):
    """
    this functions reciere todos list as a argument
    then write the latest ehanges on todos.txt file
    :param todos: list of todos
    """
    with open('todos.txt', 'w') as file:
        file.writelines(todos)