# Explanation of the Code

## Range of `n`
The statement `n = np.arange(0, 32)` creates an array of values from 0 to 31 (inclusive). This ensures that we capture 2 cycles for the slowest frequency (e.g., π/8).

## Sinusoidal Sequences

Each sequence is defined using the following formulas:

1. **x[n] = 2 · cos((π/8) · n)**
2. **x[n] = 2 · cos((π/8) · n − π/2)**
3. **x[n] = 2 · sin((π/8) · n)**
4. **x[n] = 2 · cos((π/8) · n + π/2)**
5. **x[n] = 2 · cos((π/4) · n)**
6. **x[n] = 2 · cos(π · n)**
7. **x[n] = 2 · cos((7π/4) · n)**
8. **x[n] = 2 · cos((15π/4) · n)**
9. **x[n] = 2 · cos(2π · n)**

## Plotting

- The `matplotlib` library is used to create stem plots for each sequence.
- Each sequence is plotted in a separate subplot for clarity.
- Titles, labels, and grid lines are added to improve readability.

## Expected Output

When you run the script, it will display nine plots, one for each sinusoidal sequence. Each plot will show 2 cycles of the corresponding sinusoidal waveform.
