# Team A — SimpleCalc (Assignment 1)

A simple multi-mode calculator with four functions:  
**Standard**, **Programmer**, **Scientific**, and **Converter** modes.  
Developed as a small group project by **Team A**.

# Navigation:

- 1, 2, 3, ... n: Choose what you want to do in the menu.

- Type a number → see the result.

- back / return / leave: Goes to the previous sub-menu.

- exit / stop / end: returns to main menu (for the original program)

  
  **Developers' note:** We noticed difficulty when returning to the original main menu, which houses all the sub-modules.
                    So we added these navigation keywords to help mitigate that problem.
---

## 1. Standard Mode  
**By:** Yehya & Mohammed Ali  

### Error Handling
1.  Used try-except to handle invalid numeric inputs.
2.  Checked for division by zero before dividing.
3.  displayed custom error messages instead of crashing the program.
4.  Used loops to re-ask the user for correct input after an error.
5. Handled unexpected operation names with a validation check 

### Difficulties Faced
-  Understanding how to use try-except correctly at first.
-  Making sure indentation was correct to avoid syntax errors.

---

## 2. Programmer Mode  
**By:** Mohanned & Ahmed  

### Error Handling
1. The program uses try–except to stop the program from crashing when the user enters wrong input.
2. If the user types text or symbols instead of a number, it shows a error message. 
3.  The code checks that the input is an integer only, not a float number.
4. If the user chooses a wrong menu number, the program says “Invalid choice” and asks again. 
5.  Loops are used to ask again until the user gives a correct input.
6.  The program prevents wrong base numbers and wrong formats when converting between bases.

### Difficulties Faced
-  We did not know that BITWISE functions existed in python (we rewrote the code due to that)
-  The bitwise NOT (~) result was difficult to understand because it gives negative numbers.

---

## 3. Scientific Mode  
**By:** Salim  

### Error Handling
1.  Avoided dividing by zero in functions like csc and cot because that causes an instant math error.
2.  Blocked invalid values in inverse functions like arcsin and arccos keeping inputs only between -1 and 1.
3.  Used try/except to stop the program from crashing when the user types text instead of a number.
4.  Added “back” and “stop” options so the user won’t get stuck in a loop or need to restart the program.
5.  Prevented ln(0) and ln of negative numbers, since they are not defined in real math. 

### Difficulties Faced
-  Connecting all parts together, so every function works smoothly inside the main system.
-  Keeping accuracy and simplicity, making sure the results are correct.
-  Controlling the user flow so after an error the program goes back to the right step.
-  Avoiding infinite loops when users type “back” or wrong inputs many times.
-  I made the code based on the idea that the user would enter text, but later the team decided to use numbers instead. So I faced difficulty changing the code to work with    numeric inputs.

---

## 4. Converter Mode + Code Assembly & User Interface  
**By:** Yasser  

### Error Handling
The program returns an error message when:
1. User enters incorrect values, such as a string when an integer/float was expected.  
2. User enters a float/integer when a string was expected.  
3. User enters a single input when two or more were expected (separated by a comma).  
4. User enters multiple inputs when a single input was requested.  
5. User enters a float when an integer was requested.  
6. The user tries to enter a unit that doesn't exist in the unit table.

### Difficulties Faced
- I had major issues trying to format the printed output properly.  
- The schedule/user interface for the function took the most time, even though I initially thought it would be the easiest.

---

## Team A Members
| Name | Role |
|------|------|
| Yehya | Standard Mode |
| Mohammed Ali | Standard Mode |
| Mohanned | Programmer Mode |
| Ahmed | Programmer Mode |
| Salim | Scientific Mode |
| Yasser | Converter Mode & Code integration |

---
