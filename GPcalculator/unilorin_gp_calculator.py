"""
    UNILORIN GP MANUAL CALCULATOR
    Dev: Halfboyfriend.
    Desc: This calculator was built by Devhalfboyfriend to ease and help unilorin students calculates their GP and CGPA effectively and faster.
"""

# table = [
#     {
#         "course": "Math",
#         "score":  56,
#         "unit": 2
#     },
#     {
#         "course": "Eng",
#         "score": 50,
#         "unit": 2
#     },
#     {
#         "course": "Bio",
#         "score": 40,
#         "unit": 3
#     },
#     {
#         "course": "Sci",
#         "score": 40,
#         "unit": 3
#     },
#     {
#         "course": "Mls",
#         "score": 61,
#         "unit": 2
#     },
#     {
#         "course": "Eng",
#         "score": 56,
#         "unit": 3
#     },
#     {
#         "course": "Eng",
#         "score": 40,
#         "unit": 3
#     },
#     {
#         "course": "Eng",
#         "score": 47,
#         "unit": 1
#     },
#     {
#         "course": "Eng",
#         "score": 45,
#         "unit": 2
#     },
#     {
#         "course": "Eng",
#         "score": 70,
#         "unit": 3
#     }
# ]


def calculator(table):
    """This calculator takes a dictionary input
        and calculate the scores and unit from the table.
    """
    cum_gp = 0
    for i in range(len(table)):
        if table[i]["score"] >= 70:
            cum_gp += table[i]["unit"] * 5
        elif table[i]["score"] >= 60:
            cum_gp += table[i]["unit"] * 4
        elif table[i]["score"] >= 50:
            cum_gp += table[i]["unit"] * 3
        elif table[i]["score"] >= 45:
            cum_gp += table[i]["unit"] * 2
        elif table[i]["score"] >= 40:
            cum_gp += table[i]["unit"] * 1
        else:
            cum_gp += table[i]["unit"] * 0

    return (cum_gp)



def unit_cal(table):
    """Calculate the total units of the course."""
    total = 0
    for j in range(len(table)):
        total += table[j]["unit"]
    return (total)

def update_data(course, score, unit):
    """This Function updates the dictionary data"""
    data = {}
    data["course"] = course
    data["score"] = score
    data["unit"] = unit
    return data


new_course = True
table = []
i = 0
while new_course:

    course = input("Provide the course title: ")
    score = int(input(f"whats your score in {course}? "))
    unit = int(input(f"Whats {course} unit? "))

    table.append(update_data(course, score, unit))
    i += 1
    if i == 3:
       total = calculator(table)
       total_unit = unit_cal(table)
       gp = total / total_unit
       new_course = False
       print(f"Your final GP is: {gp:3}")

