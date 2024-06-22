import pandas as pd

data = {
    'Student ID': [1, 2, 3, 4, 5, 6, 7, 8],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Hannah'],
    'Subject': ['Math', 'English', 'Math', 'Science', 'English', 'Math', 'Science', 'English'],
    'Score': [85, 78, 92, 88, 95, 75, 82, 89]
}
df = pd.DataFrame(data)

average_score = df['Score'].mean()
total_students = df['Student ID'].nunique()
subject_avg_score = df.groupby('Subject')['Score'].mean()
subject_highest_score = df.groupby('Subject')['Score'].max()
subject_lowest_score = df.groupby('Subject')['Score'].min()
top_student_overall = df.loc[df['Score'].idxmax()]['Name']
top_students_by_subject = df.loc[df.groupby('Subject')['Score'].idxmax()][['Subject', 'Name']]

print(f'Average Score: {average_score}')
print(f'Total Number of Students: {total_students}')
print(f'Average Score by Subject:\n{subject_avg_score}')
print(f'Highest Score by Subject:\n{subject_highest_score}')
print(f'Lowest Score by Subject:\n{subject_lowest_score}')
print(f'Student with Highest Overall Score: {top_student_overall}')
print(f'Top Students by Subject:\n{top_students_by_subject}')