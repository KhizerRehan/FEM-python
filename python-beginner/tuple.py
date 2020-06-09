# Tuples

a = ()
type(a)

b = (1)
type(b) # NOT A TUPLE GOTCHA!

c = (1,) # MAKE 1 ELEMENT A TUPLE ',' IS IMPORTANT
type(c)

d = (1,2,3,4,5)
type(d)

e = 1, 2, 3
type(e) # IT IS ALSO A TUPLE  ',' IS IMPORTANT


# Record as Tuple

# - TUPLES ARE IMMUTABLE:

student = ("Khizer", 25, "Urdu", "Pakistani")
print(student[0]) # Access 0th Index
print(student[1]) # Access 1th Index

# Destructuring
name, age, language, nationality = student
print(name)
print(age)
print(language)
print(nationality)

# Skip Any Value Use _
name, age, _, nationality = student
print(name)
print(age)
print(nationality)

# Method Returning a tuple
def http_statuses_code():
    return 200, "ok"

status_code, status_type = http_statuses_code()
print(status_code);
print(status_type);
