# Explanation of the Code

## Range of `n`

The statement `n = np.arange(0, 21)` creates an array of values from 0 to 20 (inclusive).

## Exponential Sequences

Each sequence is defined using the following formulas:

- **x[n] = 2 · 0.5^n**
- **x[n] = 2 · 1.5^n**
- **x[n] = 2 · (−0.5)^n**
- **x[n] = 2 · (−1.5)^n**

## Plotting

The `matplotlib` library is used to create stem plots for each sequence:

- Each sequence is plotted in a separate subplot for clarity.
- Titles, labels, and grid lines are added to improve readability.

## Expected Output

When you run the script, it will display four plots, one for each exponential sequence:

- **x[n] = 2 · 0.5^n:**  
  A decaying exponential sequence (converges to 0 as `n` increases).

- **x[n] = 2 · 1.5^n:**  
  A growing exponential sequence (diverges to infinity as `n` increases).

- **x[n] = 2 · (−0.5)^n:**  
  An alternating decaying exponential sequence (oscillates and converges to 0 as `n` increases).

- **x[n] = 2 · (−1.5)^n:**  
  An alternating growing exponential sequence (oscillates and diverges to infinity as `n` increases).
