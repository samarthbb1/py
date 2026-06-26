import pandas as pd
import io

def manage_attendance_system():
    # 1. Simulate a CSV file with student details
    csv_data = """Name,Total_Classes,Attended
Alice,50,45
Bob,50,38
Charlie,50,48
David,50,25"""
    
    # 2. Reading student details from CSV (using io.StringIO for demonstration)
    # In a real scenario, use: df = pd.read_csv('your_file.csv')
    df = pd.read_csv(io.StringIO(csv_data))

    # 3. Record new attendance (Example: Mark everyone present for one new session)
    df['Attended'] += 1
    df['Total_Classes'] += 1

    # 4. Calculate attendance percentage for each student
    df['Attendance_Percentage'] = (df['Attended'] / df['Total_Classes']) * 100

    # 5. Display the final attendance report
    print("--- Updated Student Attendance Report ---")
    print(df[['Name', 'Attended', 'Total_Classes', 'Attendance_Percentage']])

# Run the system
manage_attendance_system()
