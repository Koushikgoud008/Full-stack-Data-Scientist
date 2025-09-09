'''6. Customer Feedback Analysis

Scenario:

A company collects customer feedback in the form of ratings (1-5). Write a program to calculate the **percentage of positive feedback** (4 or 5).

Requirements:

- Use a function to calculate the positive feedback percentage.

- Handle cases where no ratings are available.

Input Example:

```python

ratings = [5, 4, 3, 5, 2, 4, 1, 5]

```

Expected Output:

```

Positive Feedback: 62.5%

```

---

 '''

def positive_feedback_percentage(ratings):
    if not ratings:
        return "No ratings available"
    
    positive_count = sum(1 for rating in ratings if rating >= 4)
    percentage = (positive_count / len(ratings)) * 100
    return f"Positive Feedback: {percentage:.1f}%"

ratings = list(map(int, input("Enter ratings separated by commas: ").split(',')))

result = positive_feedback_percentage(ratings)
print(result)
