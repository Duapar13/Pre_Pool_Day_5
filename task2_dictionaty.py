# In your student dictionary, add a units key.
# The value associated to units is an array of 3 elements.
# Each element of this array is a dictionary of 3 keys: name, credits, grade:
# The value associated with name can be one of:
# ✓ Web Development
# ✓ Network and System Administration
# ✓ Java
# The value associated with credits is a strictly positive integer.
# The value associated with grade is a letter ranging from A to E

etudiants = []

etudiants = [
    {
    "name": "Java",
    "credit": 3,
    "grade": "A"
},
{
    "name": "Web Development",
    "credit": 2,
    "grade": "B"
},
{
    "name": "Network and System Administration",
    "credit": 2,
    "grade": "B"
}
]


print(etudiants)
