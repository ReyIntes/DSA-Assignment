# DSA-Assignment
 Intes, Rey T., 1-BSCS-A

This code is to calculate mathematical expressions based on user inputs, graph those expressions, and save the results to a file.

The code begins by importing necessary libraries: matplotlib.pyplot for plotting graphs and numpy as np for numerical calculations.

Next, it defines a function calculate_expression(x, expression_num) responsible for evaluating various mathematical expressions based on the input parameters x and expression_num. Depending on the value of expression_num, it computes different expressions 

Another function, plot_graph(x_values, y_values, expression_num), is defined to plot the calculated expressions. If expression_num is 11, it plots all expressions in a single graph; otherwise, it plots a specific expression based on the provided expression_num.

The function save_results_to_file(results) is responsible for saving the calculated results to a text file named "results.txt". It reads through the list of results and writes each result to a new line in the file.

The main part of the code starts with user input for the value of x, followed by generating a sequence of x-values from 1 to the user-provided value using np.arange. Then, it reads through each expression (from 1 to 10), calculates the corresponding  y-values using calculate_expression, and stores the results.

After saving the results to a file, the user is prompted to choose an expression to graph. Depending on the choice, it either plots a single expression or all expressions using the plot_graph function.

All the images shown use 50 for the value of x:

![image](https://github.com/ReyIntes/DSA-Assignment/assets/156169140/05852a25-d335-48aa-9132-6f236f49cf7b)

![Screenshot 2024-04-01 175757](https://github.com/ReyIntes/DSA-Assignment/assets/156169140/657c9bbf-a44d-4328-9fe0-a39bfa99cb0c)

![Screenshot 2024-04-01 175831](https://github.com/ReyIntes/DSA-Assignment/assets/156169140/f94191d5-2383-428b-b1aa-d27d1803b838)

![Screenshot 2024-04-01 175842](https://github.com/ReyIntes/DSA-Assignment/assets/156169140/10c474b7-a8c9-4494-8240-c908379d620d)

![Screenshot 2024-04-01 175859](https://github.com/ReyIntes/DSA-Assignment/assets/156169140/742a2021-f528-44b1-aa79-548f92e35d8d)

![Screenshot 2024-04-01 175909](https://github.com/ReyIntes/DSA-Assignment/assets/156169140/be4ab1c1-a75e-4b67-bce6-e9052cefed02)

![Screenshot 2024-04-01 175934](https://github.com/ReyIntes/DSA-Assignment/assets/156169140/3b76081c-03a1-4fd6-84a5-472b04264211)

![Screenshot 2024-04-01 175952](https://github.com/ReyIntes/DSA-Assignment/assets/156169140/8d350583-59fb-4f2a-bbdc-6ab2f3a5a792)

![Screenshot 2024-04-01 180100](https://github.com/ReyIntes/DSA-Assignment/assets/156169140/bdc8695e-a36b-42e1-922f-3a493de93c1e)

![Screenshot 2024-04-01 180109](https://github.com/ReyIntes/DSA-Assignment/assets/156169140/33d04c47-a2c7-4d23-b727-ff4910bf9c5b)

![Screenshot 2024-04-01 180151](https://github.com/ReyIntes/DSA-Assignment/assets/156169140/3b62a1f8-75d5-4529-b373-878da1996ed2)

![Screenshot 2024-04-01 180212](https://github.com/ReyIntes/DSA-Assignment/assets/156169140/6499914b-8e05-4698-82a7-9148c17e43c0)

![Screenshot 2024-04-01 180245](https://github.com/ReyIntes/DSA-Assignment/assets/156169140/6fc9430d-b961-421a-b0ae-98292a9a2cb7)

![Screenshot 2024-04-01 180253](https://github.com/ReyIntes/DSA-Assignment/assets/156169140/7a7792ed-3733-4b7e-a284-3ea4523d7f51)

![Screenshot 2024-04-01 180450](https://github.com/ReyIntes/DSA-Assignment/assets/156169140/68c8a73d-546f-40f4-9133-54e92100866b)

![Screenshot 2024-04-01 180503](https://github.com/ReyIntes/DSA-Assignment/assets/156169140/2e350167-0544-427a-a3f4-7229fdb0010c)

![Screenshot 2024-04-01 180528](https://github.com/ReyIntes/DSA-Assignment/assets/156169140/b43b612e-ee39-461b-99ef-8ade08812710)

![Screenshot 2024-04-01 180538](https://github.com/ReyIntes/DSA-Assignment/assets/156169140/3a2c175d-f728-4a49-9a06-d03e17ce595f)

![Screenshot 2024-04-01 180557](https://github.com/ReyIntes/DSA-Assignment/assets/156169140/d02622c5-c58c-43f0-935e-63b7bc695bc4)

![Screenshot 2024-04-01 180609](https://github.com/ReyIntes/DSA-Assignment/assets/156169140/c47ad181-4399-4fce-9a3f-68653b5745d0)

![Screenshot 2024-04-01 180642](https://github.com/ReyIntes/DSA-Assignment/assets/156169140/6c46765e-9999-4130-931d-9a18ccfeeab3)

![Screenshot 2024-04-01 180652](https://github.com/ReyIntes/DSA-Assignment/assets/156169140/5a8d55fb-ac01-4446-8a43-f2e7f202d4dd)
