# OPTIMIZATION-MODEL

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: G. HARINI PRIYA

*INTERN ID*: CT04DN652

*DOMAIN*: DATA SCIENCE

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTOSH

## Candle Production Optimization using Linear Programming (PuLP)

## Project Overview

This project showcases the practical use of Linear Programming (LP) to solve a real-world business problem using Python. The focus is on a small-scale candle manufacturing business that produces two types of candles: Scented and Unscented. Each candle requires limited resources such as wax and labor hours, and the objective is to maximize profit without exceeding these constraints. This notebook presents a complete end-to-end optimization pipeline using the PuLP library.

The project is a simple and beginner-friendly introduction to operations research and optimization in Python. It's ideal for students, data science beginners, or anyone who wants to understand how LP can be applied to real-world decision-making problems. The solution is implemented in a Jupyter Notebook which includes code, outputs, markdown explanations, and key business insights.

## Problem Description

`The candle business produces`:

-	Scented Candles

-	Unscented Candles

Each candle requires a certain amount of wax and labor hours, both of which are limited.

`Given`:

-	Profit per unit:
 
     -	Scented = ₹5
   
     -  Unscented = ₹3

-	Wax needed per candle:

     -	Scented = 3 units

     -  Unscented = 2 units

-	Labor hours required per candle:

     - 	Scented = 2 hours

     -	Unscented = 1 hour

-	Available resources:

     -	Wax = 60 units

     -	Labor = 40 hours

The goal is to find the optimal number of each candle type to produce in order to maximize total profit, while not exceeding available wax and labor.

## Technologies Used

-	Python 3

-	PuLP – a linear programming modeling package

-	Jupyter Notebook – for code, visualization, and markdown explanations

## How to Run the Project

1.	Clone this repository or download the notebook file (candle_optimization.ipynb).

2.	Make sure you have Python installed.

3.	Install PuLP using pip:
`pip install pulp`

4.	Open the notebook in Jupyter or VS Code.

5.	Run all the cells to see the optimization results.

## Solution Methodology

We formulated a Linear Programming model with:

-	`Decision Variables`: Number of scented and unscented candles to produce.

-	`Objective Function`: Maximize total profit from both candle types.

-	`Constraints`:

     -	Total wax used must not exceed 60 units.

     -	Total labor used must not exceed 40 hours.

The model is solved using PuLP’s built-in solver. The solution includes:

-	Optimal quantities of both types of candles

-	Maximum achievable profit under the given constraints

-	Model status verification

## Solution 

`After solving the model, we obtain`:

-	Optimal Scented Candles: `value of x`

-	Optimal Unscented Candles: `value of y`

-	Maximum Profit: `₹ value of objective function`

These values are dynamically computed and printed by the notebook.

## Business Insights

-	The model highlights how limited resources can be strategically allocated to maximize business returns.

-	By converting a business problem into a mathematical model, even small businesses can make informed decisions.

-	Linear Programming is especially useful for inventory management, production planning, logistics, and resource allocation.

-	This solution framework can be scaled up to include more constraints such as packaging limits, demand restrictions, cost changes, or seasonal variation in profit margins.

## Conclusion

This project demonstrates the effectiveness of Linear Programming in solving small business problems. It is a simple yet powerful tool for decision-making and resource optimization. Whether you're managing a factory, planning deliveries, or allocating staff, LP techniques like this provide a structured and scalable way to maximize efficiency and profit.
