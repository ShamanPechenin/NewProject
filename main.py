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


def single_newton_iteration(func: Callable, approx_x: float) -> float:
    """
    Single iteration of newthon method to solve f(x)=0 for x
    :param func:
    :param approx_x:
    :return:
    """
    return approx_x - func(approx_x)/calculate_derivative(func, approx_x)


def newton_method(func: Callable, approx_x: float, n_iter: int) -> float:
    for i in range(n_iter):
        approx_x = single_newton_iteration(func, approx_x)
    return approx_x


def brute_force(func: Callable, x_range: tuple[float, float], n_calls: int):
    """
    Solves f(x)=0 for x using brute force method
    :param func:
    :param x_range:
    :param n_calls:
    :return:
    """
    best_x = None
    best_diff = None
    for i in range(n_calls):
        x = x_range[0]+i*(x_range[1]-x_range[0])/n_calls
        diff = abs(func(x))
        if best_diff is None:
            best_diff = diff
            best_x = x
            continue

        if diff < best_diff:
            best_diff = diff
            best_x = x
    return best_x


def get_equation_from_user() -> Callable:
    variants = {"1": 2, "2": 2, "3": 2}
    user_selection = input("\n1. a*x=b\n2. x^a=b\n3. a^x=b\nSelect equation to solve: ").strip()
    if user_selection not in variants:
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


def get_method_from_user() -> Callable:
    user_selection = input("\n1. Newton method\n2. Brute-force method\nSelect method: ").strip()
    if user_selection == "1":
        approx_x = float(input("Enter approximate x value: ").strip())
        n_iter = int(input("Enter number of iterations: ").strip())
        return lambda f: newton_method(f, approx_x=approx_x, n_iter=n_iter)
    elif user_selection == "2":
        range_start = float(input("Enter x range start: ").strip())
        range_end = float(input("Enter x range end: ").strip())
        n_calls = int(input("Enter number of calls: ").strip())
        return lambda f: brute_force(f, x_range=(range_start, range_end), n_calls=n_calls)


def solve(func: Callable, solver: Callable) -> dict[str: float]:
    approx_x = solver(func)
    y_at_x = func(approx_x)

    return {"x": approx_x, "y_at_x": y_at_x}


def pretty_print_solution(solution: dict[str: float]):
    print(f"Approximated x is: {solution['x']}")
    print(f"Value of function at x is: {solution['y_at_x']}")


def interactive_main():
    while True:
        func = get_equation_from_user()
        solver = get_method_from_user()
        solution = solve(func, solver)
        pretty_print_solution(solution)
        print("-------------------------------")
        if input("Continue?[y/n]: ").lower() != "y":
            break
        print("-------------------------------")


if __name__ == '__main__':
    interactive_main()
