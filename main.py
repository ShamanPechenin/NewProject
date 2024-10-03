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


def newton_iteration(func: Callable, approx_x: float, y: float) -> float:
    """
    Solves f(x)=y for x using newton iteration method
    :param func:
    :param approx_x:
    :param y:
    :return:
    """
    return approx_x - (func(approx_x)-y)/calculate_derivative(func, approx_x)


def brute_force(func: Callable, y: float, x_range: tuple[float, float], n_calls: int):
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
        diff = func(x)-y
        if best_diff is None:
            best_diff = y
            best_x = x
            continue

        if abs(diff) < best_diff:
            best_diff = y
            best_x = x
    return best_x


def get_equation_from_user():
    pass


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
