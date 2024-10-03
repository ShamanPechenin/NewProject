from typing import Callable


def calculate_derivative(func: Callable, point: float, eps=1e-9) -> float:
    """
    Calculates d f(x)/dx at a point
    :param func:
    :param point:
    :param eps:
    :return:
    """
    return (func(point+eps)-func(point))/eps


def newton_iteration(func: Callable, approx_x: float) -> float:
    """
    Solves f(x)=0 for x using newton iteration method
    :param func:
    :param approx_x:
    :return:
    """
    return approx_x - func(approx_x)/calculate_derivative(func, approx_x)


def brute_force(func: Callable, x_range: tuple[float, float], n_calls: int):
    """
    Solves f(x)=y for x using brute force method
    :param func:
    :param y:
    :param x_range:
    :param n_calls:
    :return:
    """
    best_x = None
    best_diff = None
    for i in range(n_calls):
        x = x_range[0]+i*(x_range[1]-x_range[0])/n_calls
        diff = func(x)
        if best_diff is None:
            best_diff = diff
            best_x = x
            continue

        if abs(diff) < best_diff:
            best_diff = diff
            best_x = x
    return best_x


def get_equation_from_user():
    variants = {"1": 2, "2": 2, "3": 2}
    user_selection = input("\n1. a*x=b\n2. x^a=b\n3. a^x=b\nSelect equation to solve: ").strip()
    if not user_selection in variants:
        print("Invalid selection. Try again.")
        raise ValueError
    constants = []
    for i in range(variants[user_selection]):
        user_input = float(input(f"Enter constant {chr(97+i)} value: ").strip())
        constants.append(user_input)
    if user_selection == "1":
        return lambda x: constants[0] * x - constants[1]
    elif user_selection == "2":
        return lambda x: x ** constants[0] - constants[1]
    elif user_selection == "3":
        return lambda x: constants[0] ** x - constants[1]


def get_method_from_user():
    pass


def solve(func, method, params):
    pass


def pretty_print_solution(solution):
    pass


def interactive_main():
    while True:
        func = get_equation_from_user()
        method, params = get_method_from_user()
        solution = solve(func, method, params)
        pretty_print_solution(solution)
        print("-------------------------------")
        if input("Continue?[y/n]: ").lower() != "y":
            break
        print("-------------------------------")

if __name__ == '__main__':
    interactive_main()
