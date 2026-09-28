# Multi-Utility Toolkit

A comprehensive command-line Python application featuring a wide range of utility modules to handle everyday programming tasks, from mathematical computations and date-time management to random data generation, file handling, and unique identifier creation.

---

## Features

The toolkit is organized into multiple modules, accessible via an interactive command-line interface (CLI)[cite: 6]:

* **1. Date & Time Operations** (`date_time.py`)[cite: 1, 6]
  * Display current date and time[cite: 1, 6].
  * Calculate the difference between two dates/times[cite: 1, 6].
  * Format dates into custom formats[cite: 1, 6].
  * Built-in interactive stopwatch[cite: 1, 6].
  * Countdown timer[cite: 1, 6].

* **2. Mathematical Operations** (`math_module.py`)[cite: 3, 6]
  * Calculate factorials[cite: 3, 6].
  * Solve compound interest problems[cite: 3, 6].
  * Perform trigonometric calculations (sin, cos, tan and their inverses)[cite: 3, 6].
  * Find the area of geometric shapes (Circle, Square)[cite: 3, 6].

* **3. Random Data Generation** (`randm_module.py`)[cite: 4, 6]
  * Generate random floating-point and integer numbers[cite: 4, 6].
  * Create lists populated with random numbers[cite: 4, 6].
  * Generate secure random passwords with customizable length and character sets[cite: 4, 6].
  * Generate random One-Time Passwords (OTPs)[cite: 4, 6].

* **4. Unique Identifiers (UUID)** (`uuid.py`)[cite: 5, 6]
  * Generate UUID version 3 (namespace-based)[cite: 5, 6].
  * Generate UUID version 4 (random)[cite: 5, 6].
  * Generate UUID version 5 (namespace-based with SHA-1)[cite: 5, 6].

* **5. File Operations** (`file_oprtr.py`)[cite: 2, 6]
  * Create new files safely[cite: 2, 6].
  * Write text data to files[cite: 2, 6].
  * Read file contents[cite: 2, 6].
  * Append data to existing files[cite: 2, 6].

* **6. Module Inspection**[cite: 6]
  * Explore attributes and methods of any built-in or custom module dynamically using Python's `dir()` function[cite: 6].

---

## Project Structure

```text
├── project7.py         # Main entry point and interactive CLI menu loop
└── modules/
    ├── date_time.py    # Date, time, stopwatch, and timer functionalities
    ├── math_module.py  # Advanced math, compound interest, and geometry
    ├── randm_module.py # Random numbers, lists, passwords, and OTPs
    ├── file_oprtr.py   # Basic file input/output management
    └── uuid.py         # UUID generation helpers (v3, v4, v5)
