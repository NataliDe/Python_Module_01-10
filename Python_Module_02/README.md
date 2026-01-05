*This project has been created as part of the 42 curriculum by <ndemkiv>.*

# Garden Guardian  
## Data Engineering for Smart Agriculture
---

## Description

**Garden Guardian** is an educational Python project focused on learning and mastering
**error handling and defensive programming** through the theme of *smart agriculture*.

The goal of this project is to simulate **robust data pipelines** for agricultural systems
that must handle unreliable inputs such as faulty sensors, invalid user data, or unexpected
runtime errors. Instead of crashing, the system is designed to **detect problems, report them
clearly, recover gracefully, and continue running**.

Throughout the exercises, the project demonstrates:
- Validation of external data (sensor readings, user input)
- Handling multiple types of runtime errors
- Creation and usage of custom exception types
- Guaranteed resource cleanup using `finally`
- Raising meaningful errors when invalid conditions are detected
- Building a small but resilient management system (`GardenManager`)

Each exercise builds on the previous one, culminating in a complete garden management
system that combines all learned techniques.

Each exercise is isolated in its own directory, as required.

---

## Instructions

### Requirements
- Python **3.10 or higher**
- `flake8` compliance
- No external libraries required

### Running the programs

Each exercise can be run independently.

Example:
```bash
python3 ex0/ft_first_exception.py
python3 ex1/ft_different_errors.py
python3 ex5/ft_garden_management.py
```
## Resources

### Programming & Python

* Python Official Documentation: [https://docs.python.org/3/](https://docs.python.org/3/)
* PEP 8 — Style Guide for Python Code: [https://peps.python.org/pep-0008/](https://peps.python.org/pep-0008/)
* Real Python — Object-Oriented Programming: [https://realpython.com/python3-object-oriented-programming/](https://realpython.com/python3-object-oriented-programming/)

### Object-Oriented Programming Concepts

* Inheritance and Composition: [https://realpython.com/inheritance-composition-python/](https://realpython.com/inheritance-composition-python/)
* Encapsulation in Python: [https://www.geeksforgeeks.org/encapsulation-in-python/](https://www.geeksforgeeks.org/encapsulation-in-python/)

### AI Usage 
Specifically, AI was used to:
clarify Python exception-handling concepts
review and improve code readability
help structure explanations and documentation
All generated content was:
reviewed line by line
tested manually
fully understood before inclusion