import pandas as pd

data = {
        'Name': ['John', 'Bob', 'Valentyn', 'Anna', 'Marks'],
        'Age': [17, 18, 21, 55, 60],
        'Gender': ['Man', 'Man', 'Man', 'Woman', 'Man'],
        'Score': [69, 50, 89, 88, 86]
    }

def work_with_dict():
    df = pd.DataFrame(data)
    print(df[:5])
    
def test():
    students = pd.DataFrame(data)
    avg_age = students['Age'].mean()
    print(f"Avg age {avg_age}")
    print(students[students['Score']>80])
    students.at[3, 'Score'] = 95
    print(students)
    ages = students['Age']
    print(ages.max())
    
def delete_from_students():
    students = pd.DataFrame(data)
    new_df = students = students[students["Name"] != "John"]
    print(new_df)
    new_df.to_csv("students.csv")
    
delete_from_students()