user = dict()

user["name"] = 'Paul'
user["age"] = 12
user["foo"] = 'bar'

print(user)
# user.pop("foo")
del user["foo"]
print("foo" in user)

print(user["age"])
