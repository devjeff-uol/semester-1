# Week 1.2, Session 1: Task 5

rivers = {
    "London": "Thames",
    "Leeds": "Aire",
    "Liverpool": "Mersey"
}

print(rivers)

# Add two new entries to the rivers database
rivers["Shanghai"] = "Yangtze"
rivers["Lanzhou"] = "Yellow River"

# Display all the keys
print("keys: ", rivers.keys())

# Display all the values
print("values: ", rivers.values())

# Display all the key:value pairs, as tuples
print("key:value pairs: ", rivers.items())

# Delete an entry from the rivers database
rivers.pop("Liverpool")
print("key:value pairs after deletion: ", rivers.items())