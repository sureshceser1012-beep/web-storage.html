```python
import pandas as pd


# Create table with 10 rows
data = {
    "id": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "name": [
        "John", "David", "Smith", "Emma", "James",
        "Alice", "Robert", "Mary", "Daniel", "Sophia"
    ],
    "age": [25, 30, 22, 28, 35, 24, 40, 32, 27, 29],
    "city": [
        "New York", "Chicago", "Boston", "Houston", "Dallas",
        "Miami", "Seattle", "Austin", "Denver", "Phoenix"
    ],
    "country": [
        "USA", "USA", "UK", "USA", "Canada",
        "USA", "USA", "India", "USA", "UK"
    ]
}

df = pd.DataFrame(data)


# Add a new row
def add_row(table, new_row):
    return pd.concat(
        [table, pd.DataFrame([new_row])],
        ignore_index=True
    )


# Calculate total rows and average age
def calculate_statistics(table):
    total_rows = len(table)
    average_age = table["age"].mean()

    print("Total rows:", total_rows)
    print("Average age:", average_age)


# Filter USA records and sort by age descending
def filter_usa(table):
    result = table[table["country"] == "USA"]
    result = result.sort_values(
        by="age",
        ascending=False
    )

    return result


# Add a new row
new_person = {
    "id": 11,
    "name": "Michael",
    "age": 31,
    "city": "Los Angeles",
    "country": "USA"
}

df = add_row(df, new_person)

# Display statistics
calculate_statistics(df)

# Display USA records
print("\nUSA Records:")
print(filter_usa(df))
```