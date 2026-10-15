# ==========================================
# LAB 3: FUNCTIONS, DICTIONARIES, AND DATA STRUCTURES
# Advanced Python Course - Week 3
# ==========================================
#
# INSTRUCTIONS:
# - Section A: Complete the function bodies (skeleton provided)
# - Section B & C: Write entire functions from scratch
# - Function names MUST match exactly or tests will fail
# - Test your code by running: python test_lab3.py
# - Submit by pushing to your GitHub repository
# ==========================================

# ==========================================
# SECTION A: FUNCTIONS WITH GUIDANCE (18 points)
# Function skeleton provided - fill in the body
# ==========================================

# ==========================================
# EXERCISE 1: Temperature Converter (6 points)
# ==========================================
def celsius_to_fahrenheit(celsius):
    """
    Convert temperature from Celsius to Fahrenheit.

    Formula: Fahrenheit is Celsius x 9/5 + 32

    Args:
        Celsius (float): Temperature in Celsius

    Returns:
        float: Temperature in Fahrenheit

    Example:
        celsius_to_fahrenheit(0) returns 32.0
        celsius_to_fahrenheit(100) returns 212.0
    """
    fahrenheit = celsius * 9 / 5 + 32

    return fahrenheit


# ==========================================
# EXERCISE 2: Dictionary Lookup with Default (6 points)
# ==========================================
def get_student_grade(grades, student_name):
    grade = grades.get(student_name, 0)

    return grade


# ==========================================
# EXERCISE 3: Format Person Information (6 points)
# ==========================================
def format_person(name, age, city):
    formatted = f"Name: {name}, Age: {age}, City: {city}"

    return formatted


# ==========================================
# SECTION B: WRITE COMPLETE FUNCTIONS (52 points)
# Write the entire function from scratch
# ==========================================

# ==========================================
# EXERCISE 4: Calculate Average (6 points)
def calculate_average(numbers):
    return sum(numbers) / len(numbers)


# ==========================================
# EXERCISE 5: Clean Filename (6 points)
def clean_filename(filename):
    return filename.strip().lower()

# ==========================================
# EXERCISE 6: Count File Extensions (10 points)
# ==========================================
def count_extensions(filenames):
    counts = {}
    for name in filenames:
        ext = name.split(".")[-1]
        counts[ext] = counts.get(ext, 0) + 1
    return counts

# ==========================================
# EXERCISE 7: Filter Passing Students (10 points)
def filter_passing_students(grades):
    passing = {}
    for name, score in grades.items():
        if score >= 60:
            passing[name] = score
    return passing

# ==========================================
# EXERCISE 8: Analyze Numbers (10 points)
# ==========================================
def analyze_numbers(numbers):
    average = sum(numbers) / len(numbers)
    return (min(numbers), max(numbers), average)

# ==========================================
# EXERCISE 9: Read Numbers from File (10 points)
# ==========================================
def read_numbers_from_file(filename):
    numbers = []
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if line:
                numbers.append(int(line))
    return numbers

# ==========================================
# SECTION C: ADVANCED INTEGRATION (50 points)
# Complex functions combining multiple concepts
# ==========================================

# ==========================================
# EXERCISE 10: Shopping Cart Total (10 points)
# ==========================================
def calculate_cart_total(cart):
    total = 0
    for item, (price, quantity) in cart.items():
        total += price * quantity
    return total

# ==========================================
# EXERCISE 11: Generate Grade Report (20 points)
# ==========================================
def generate_grade_report(scores):
    lines = []
    for name, score in scores.items():
        if score >= 90:
            letter = "A"
        elif score >= 80:
            letter = "B"
        elif score >= 70:
            letter = "C"
        elif score >= 60:
            letter = "D"
        else:
            letter = "F"
        lines.append(f"Student: {name}, Score: {score}, Grade: {letter}")
    return "\n".join(lines)


# ==========================================
# EXERCISE 12: Analyze Log File (20 points)
# ==========================================
def analyze_log_file(filename):
    result = {
        "total_lines": 0,
        "levels": {"ERROR": 0, "WARNING": 0, "INFO": 0}
    }
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            result["total_lines"] += 1
            level = line.split(": ")[0]
            if level in result["levels"]:
                result["levels"][level] += 1
    return result

                    
# =
# DO NOT MODIFY BELOW THIS LINE
# ==========================================
if __name__ == "__main__":
    print("Run 'python test_lab3.py' to test your solutions!")
