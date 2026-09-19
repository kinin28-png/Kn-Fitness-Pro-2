def calculate_bmr(weight, height, age, gender):
    if str(gender).lower() == "male":
        return (10 * weight) + (6.25 * height * 100) - (5 * age) + 5
    else:
        return (10 * weight) + (6.25 * height * 100) - (5 * age) - 161