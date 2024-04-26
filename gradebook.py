"""Gradebook exercise"""

lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0],
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0],
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0],
}

students = [lloyd, alice, tyler]


def average(numbers: list[int]) -> float:
    """function to return average from provided list of integers"""
    return float(sum(numbers)) / len(numbers)


def get_average(student: dict) -> float:
    """function to return students weighted number grade"""
    return (
        average(student["homework"]) * 0.1
        + average(student["quizzes"]) * 0.3
        + average(student["tests"]) * 0.6
    )


def get_letter_grade(score: float) -> str:
    """function to return letter grade based on provided number grade"""
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"


def get_class_average(students: list[dict]) -> float:
    """function to determin the overall class average number grade"""
    results = []
    for student in students:
        results.append(get_average(student))
    return average(results)


print(get_class_average(students))
print(get_letter_grade(get_class_average(students)))
