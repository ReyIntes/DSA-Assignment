# DSA-Assignment
 Intes, Rey T., 1-BSCS-A

This code is to calculate mathematical expressions based on user inputs, graph those expressions, and save the results to a file.

The code begins by importing necessary libraries: matplotlib.pyplot for plotting graphs and numpy as np for numerical calculations.

Next, it defines a function calculate_expression(x, expression_num) responsible for evaluating various mathematical expressions based on the input parameters x and expression_num. Depending on the value of expression_num, it computes different expressions 

Another function, plot_graph(x_values, y_values, expression_num), is defined to plot the calculated expressions. If expression_num is 11, it plots all expressions in a single graph; otherwise, it plots a specific expression based on the provided expression_num.

The function save_results_to_file(results) is responsible for saving the calculated results to a text file named "results.txt". It reads through the list of results and writes each result to a new line in the file.

The main part of the code starts with user input for the value of x, followed by generating a sequence of x-values from 1 to the user-provided value using np.arange. Then, it reads through each expression (from 1 to 10), calculates the corresponding  y-values using calculate_expression, and stores the results.

After saving the results to a file, the user is prompted to choose an expression to graph. Depending on the choice, it either plots a single expression or all expressions using the plot_graph function.

![image](https://github.com/ReyIntes/DSA-Assignment/assets/156169140/05852a25-d335-48aa-9132-6f236f49cf7b)
