import matplotlib.pyplot as plt
import numpy as np

def calculate_expression(x, expression_num):
    if expression_num == 1:
        return x**2 + 7*x + 2
    elif expression_num == 2:
        return 3*x + 2
    elif expression_num == 3:
        return x**2
    elif expression_num == 4:
        return x**3
    elif expression_num == 5:
        return x**5
    elif expression_num == 6:
        return x**3 + 2*x**2 + x + 10
    elif expression_num == 7:
        return x**4 - 3*x**3 + 2*x**2 - x + 11
    elif expression_num == 8:
        return np.sin(x)
    elif expression_num == 9:
        return np.cos(x)
    elif expression_num == 10:
        return x**5 + 4*x**4 + x**3 - 2*x**2 + 100

def plot_graph(x_values, y_values, expression_num):
    if expression_num == 11:
        expressions = ["x^2 + 7x + 2", "3x + 2", "x^2", "x^3",
                       "x^5", "x^3 + 2x^2 + x + 10", "x^4 - 3x^3 + 2x^2 - x + 11",
                       "sin(x)", "cos(x)", "x^5 + 4x^4 + x^3 - 2x^2 + 100"]
        for i, y_vals in enumerate(y_values):
            plt.plot(x_values, y_vals, label=expressions[i])
        plt.legend()
    else:
        expression = ["x^2 + 7x + 2", "3x + 2", "x^2", "x^3",
                      "x^5", "x^3 + 2x^2 + x + 10", "x^4 - 3x^3 + 2x^2 - x + 11",
                      "sin(x)", "cos(x)", "x^5 + 4x^4 + x^3 - 2x^2 + 100"]
        plt.plot(x_values, y_values, label=expression[expression_num-1])
        plt.legend()
    plt.show()

def save_results_to_file(results):
    with open("results.txt", "w") as f:
        for result in results:
            f.write(str(result) + "\n")

if __name__ == "__main__":
    x = int(input("Enter a value for x (1-50): "))
    
    x_values = np.arange(1, x+1)
    results = []
    
    for i in range(1, 11):
        y_values = [calculate_expression(val, i) for val in x_values]
        results.append(y_values)
    
    save_results_to_file(results)
    
    expression_num = int(input("Which expression to graph (1-10, 11 for all)? "))
    
    if expression_num == 11:
        plot_graph(x_values, results, expression_num)
    else:
        y_values = results[expression_num-1]
        plot_graph(x_values, y_values, expression_num)