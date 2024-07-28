import sqlite3

# Connect to SQLite
connection = sqlite3.connect("clubs.db")

# Create a cursor object to insert records, create table
cursor = connection.cursor()

# Create the table
table_info = """
CREATE TABLE IF NOT EXISTS TECH_CLUBS (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NAME VARCHAR(50),
    DESCRIPTION TEXT,
    YEAR_INAUGURATED INTEGER,
    PAST_EVENTS TEXT,
    BUDGET DECIMAL(10, 2),
    UPCOMING_EVENTS TEXT,
    HOW_TO_ENROLL TEXT
);
"""
cursor.execute(table_info)

# Insert records for each club
clubs_data = [
    ("IEEE",
     "The Institute of Electrical and Electronics Engineers student branch focuses on electrical, electronic, and computer science engineering.",
     2017,
     "Annual Tech Symposium, IoT Workshop, Circuit Design Competition", 50000.00,
     "AI in Healthcare Seminar, Robotics Showcase",
     "Visit the IEEE office in the Engineering building or email ieee@college.edu"),

    ("Infinitix", "A coding club that promotes competitive programming and software development skills.", 2018,
     "24-hour Hackathon, Code Golf Challenge, Mobile App Development Workshop", 35000.00,
     "Web Development Bootcamp, Competitive Coding Contest",
     "Register on the college portal or contact infinitix@college.edu"),

    ("TechCider", "An innovation hub that focuses on emerging technologies and entrepreneurship.", 2019,
     "Startup Pitch Competition, AR/VR Demo Day, Tech Entrepreneurship Workshop", 40000.00,
     "Blockchain Basics Seminar, Innovation Challenge 2024",
     "Apply through the TechCider website or visit their stall during orientation week"),

    (
    "Manthan", "A think-tank that organizes debates, discussions, and projects on the impact of technology on society.",
    2017,
    "Ethics in AI Debate, Tech Policy Roundtable, Digital Privacy Awareness Campaign", 30000.00,
    "Future of Work Symposium, Green Tech Expo",
    "Submit an application essay to manthan@college.edu or attend an open house session")
]

cursor.executemany('''
    INSERT INTO TECH_CLUBS (NAME, DESCRIPTION, YEAR_INAUGURATED, PAST_EVENTS, BUDGET, UPCOMING_EVENTS, HOW_TO_ENROLL)
    VALUES (?, ?, ?, ?, ?, ?, ?)
''', clubs_data)
g
# Display all the records
print("The inserted records are:")
data = cursor.execute('''SELECT * FROM TECH_CLUBS''')
for row in data:
    print(row)

# Commit changes in the database
connection.commit()

# Close the connection
connection.close()