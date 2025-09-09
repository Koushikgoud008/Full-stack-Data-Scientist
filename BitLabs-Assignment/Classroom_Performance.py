'''3. Classroom Performance Tracker

Scenario:A teacher wants to track student performance. Write a program to calculate the **average marks** of students and identify the **top performer**.

Requirements:

- Use a function to calculate the average marks.

- Identify the student with the highest average.

- Optional: Implement a `Student` class to handle this logic.

Input Example:

students = {"John": [85, 78, 92], "Alice": [88, 79, 95], "Bob": [70, 75, 80]}

Expected Output:

Average Marks: {"John": 85, "Alice": 87.33, "Bob": 75}

Top Performer: "Alice"'''

import statistics as st
class Student:
    def __init__(self,myDict):
        self.myDict = myDict
    def alo(self):
        res_dict = {}
        top_res = ''
        top_res_val = 0
        for name in self.myDict:
            mean_value = round(st.mean(self.myDict[name]),2)
            res_dict[name] = mean_value
            if top_res_val < mean_value :
                top_res = name
                top_res_val = mean_value
        print(f"Average Marks: {res_dict}")
        print(f"Top performer: {top_res}")

students = {"John": [85, 78, 92], "Alice": [88, 79, 95], "Bob": [70, 75, 80]}

obj = Student(students)
obj.alo()