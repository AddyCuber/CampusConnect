import sqlite3

# Connect to SQLite
connection = sqlite3.connect("clubs.db")

# Create a cursor object to insert records, create table
cursor = connection.cursor()

# Create the table
tables ={ 
"TECH_CLUBS": """
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
""",
 "STUCO_CLUBS": """
        CREATE TABLE IF NOT EXISTS STUCO_CLUBS (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NAME VARCHAR(50),
            DESCRIPTION TEXT,
            YEAR_INAUGURATED INTEGER,
            PAST_EVENTS TEXT,
            BUDGET DECIMAL(10, 2),
            UPCOMING_EVENTS TEXT,
            HOW_TO_ENROLL TEXT
        );
    """,
    "CULTURAL_CLUBS": """
        CREATE TABLE IF NOT EXISTS CULTURAL_CLUBS (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NAME VARCHAR(50),
            DESCRIPTION TEXT,
            YEAR_INAUGURATED INTEGER,
            PAST_EVENTS TEXT,
            BUDGET DECIMAL(10, 2),
            UPCOMING_EVENTS TEXT,
            HOW_TO_ENROLL TEXT
        );
    """,
    "SPORTS_CLUBS": """
        CREATE TABLE IF NOT EXISTS SPORTS_CLUBS (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NAME VARCHAR(50),
            DESCRIPTION TEXT,
            YEAR_INAUGURATED INTEGER,
            PAST_EVENTS TEXT,
            BUDGET DECIMAL(10, 2),
            UPCOMING_EVENTS TEXT,
            HOW_TO_ENROLL TEXT
        );
    """,
    "E_CELL": """
        CREATE TABLE IF NOT EXISTS E_CELL (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NAME VARCHAR(50),
            DESCRIPTION TEXT,
            YEAR_INAUGURATED INTEGER,
            PAST_EVENTS TEXT,
            BUDGET DECIMAL(10, 2),
            UPCOMING_EVENTS TEXT,
            HOW_TO_ENROLL TEXT
        );
    """,
    "ROTRACT_CLUBS": """
        CREATE TABLE IF NOT EXISTS ROTRACT_CLUBS (
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
}

# Execute SQL command to create each table
for table, command in tables.items():
    cursor.execute(command)

# Insert records for each club
clubs_data = {
    "TECH_CLUBS": [
        ("IEEE", "The Institute of Electrical and Electronics Engineers student branch focuses on electrical, electronic, and computer science engineering.", 2017, "Annual Tech Symposium, IoT Workshop, Circuit Design Competition", 50000.00, "AI in Healthcare Seminar, Robotics Showcase", "Visit the IEEE office in the Engineering building or email ieee@college.edu"),
        ("Infinitix", "A coding club that promotes competitive programming and software development skills.", 2018, "24-hour Hackathon, Code Golf Challenge, Mobile App Development Workshop", 35000.00, "Web Development Bootcamp, Competitive Coding Contest", "Register on the college portal or contact infinitix@college.edu"),
        ("TechCider", "An innovation hub that focuses on emerging technologies and entrepreneurship.", 2019, "Startup Pitch Competition, AR/VR Demo Day, Tech Entrepreneurship Workshop", 40000.00, "Blockchain Basics Seminar, Innovation Challenge 2024", "Apply through the TechCider website or visit their stall during orientation week"),
        ("Manthan", "A think-tank that organizes debates, discussions, and projects on the impact of technology on society.", 2017, "Ethics in AI Debate, Tech Policy Roundtable, Digital Privacy Awareness Campaign", 30000.00, "Future of Work Symposium, Green Tech Expo", "Submit an application essay to manthan@college.edu or attend an open house session")
    ],
    "STUCO_CLUBS": [
        ("STUCO General Body", "The Student Council General Body oversees all student council activities and ensures the student body is represented.", 2018, "Orientation Week, Annual Fest, Elections", 45000.00, "New Member Induction, Annual Review Meeting", "Visit the student council office or email stuco@college.edu"),
        ("STUCO Editorial", "The Student Council Editorial team manages all publications and written content for the council.", 2019, "Monthly Newsletter, Annual Yearbook", 10000.00, "Magazine Launch", "Visit the student council office or email editorial@college.edu"),
        ("STUCO Sponsorship", "The Student Council Sponsorship team handles all sponsorship activities and relations.", 2018, "Sponsorship Drive, Fundraising Events", 20000.00, "Sponsorship Meet", "Contact the student council office or email sponsorship@college.edu"),
        ("STUCO Marketing", "The Student Council Marketing team is responsible for promoting council events and activities.", 2019, "Social Media Campaigns, Event Promotions", 15000.00, "Marketing Workshop", "Visit the student council office or email marketing@college.edu"),
        ("STUCO Creatives", "The Student Council Creatives team manages all creative content and designs for the council.", 2018, "Poster Design, Event Branding", 12000.00, "Creative Workshop", "Visit the student council office or email creatives@college.edu"),
        ("STUCO PR", "The Student Council PR team handles public relations and communication for the council.", 2019, "Press Releases, Media Relations", 13000.00, "PR Training Session", "Visit the student council office or email pr@college.edu")
    ],
    "CULTURAL_CLUBS": [
        ("Cultural General Body", "The Cultural Club General Body organizes and oversees cultural events and activities.", 2019, "Cultural Fest, Dance Competition, Music Night", 30000.00, "Cultural Week, Art Exhibition", "Join during the cultural fest or contact cultural@college.edu"),
        ("Cultural Sponsorship", "The Cultural Club Sponsorship team manages sponsorship and fundraising for cultural events.", 2018, "Sponsorship Drive, Fundraising Events", 20000.00, "Sponsorship Meet", "Contact the cultural club office or email culturalsponsorship@college.edu"),
        ("Cultural Logistics", "The Cultural Club Logistics team handles all logistical aspects of cultural events.", 2019, "Event Setup, Coordination", 15000.00, "Logistics Training", "Visit the cultural club office or email culturallogistics@college.edu")
    ],
    "SPORTS_CLUBS": [
        ("Sports General Body", "The Sports Club General Body oversees all sports activities and events.", 2017, "Annual Sports Meet, Inter-College Tournament, Sports Workshop", 50000.00, "Fitness Bootcamp, Marathon", "Sign up at the sports office or email sports@college.edu"),
        ("Sports Hospitality", "The Sports Club Hospitality team manages all hospitality arrangements for sports events.", 2018, "Guest Management, Player Accommodation", 25000.00, "Hospitality Workshop", "Visit the sports office or email sportshospitality@college.edu"),
        ("Sports Sponsorship", "The Sports Club Sponsorship team handles sponsorship and fundraising for sports events.", 2019, "Sponsorship Drive, Fundraising Events", 20000.00, "Sponsorship Meet", "Contact the sports office or email sportssponsorship@college.edu"),
        ("Sports Marketing", "The Sports Club Marketing team promotes sports events and activities.", 2018, "Social Media Campaigns, Event Promotions", 15000.00, "Marketing Workshop", "Visit the sports office or email sportsmarketing@college.edu"),
        ("Sports Creatives", "The Sports Club Creatives team designs and manages creative content for sports events.", 2019, "Poster Design, Event Branding", 12000.00, "Creative Workshop", "Visit the sports office or email sportscreatives@college.edu"),
        ("Sports PR", "The Sports Club PR team handles public relations for sports events.", 2017, "Press Releases, Media Relations", 13000.00, "PR Training Session", "Visit the sports office or email sportspr@college.edu")
    ],
    "E_CELL": [
        ("E-cell General Body", "The Entrepreneurship Cell General Body oversees all activities and events.", 2020, "Startup Bootcamp, Innovation Fair, Investor Pitch", 60000.00, "Startup Showcase, Entrepreneur Talks", "Register through the E-cell website or contact ecell@college.edu"),
        ("E-cell Editorial", "The Entrepreneurship Cell Editorial team manages all publications and written content.", 2019, "Monthly Newsletter, Blog", 10000.00, "Magazine Launch", "Visit the E-cell office or email ecelleditorial@college.edu"),
        ("E-cell Sponsorship", "The Entrepreneurship Cell Sponsorship team handles sponsorship and fundraising activities.", 2018, "Sponsorship Drive, Fundraising Events", 20000.00, "Sponsorship Meet", "Contact the E-cell office or email ecellsponsorship@college.edu"),
        ("E-cell Marketing", "The Entrepreneurship Cell Marketing team promotes events and activities.", 2019, "Social Media Campaigns, Event Promotions", 15000.00, "Marketing Workshop", "Visit the E-cell office or email ecellmarketing@college.edu"),
        ("E-cell Creatives", "The Entrepreneurship Cell Creatives team manages all creative content and designs.", 2018, "Poster Design, Event Branding", 12000.00, "Creative Workshop", "Visit the E-cell office or email ecellcreatives@college.edu"),
        ("E-cell PR", "The Entrepreneurship Cell PR team handles public relations and communication.", 2019, "Press Releases, Media Relations", 13000.00, "PR Training Session", "Visit the E-cell office or email ecellpr@college.edu"),
        ("E-cell Research and Development", "The Entrepreneurship Cell R&D team focuses on research and development projects.", 2020, "Market Research, Product Development", 20000.00, "R&D Workshop", "Visit the E-cell office or email ecellrandd@college.edu")
    ],
    "ROTRACT_CLUBS": [
        ("Rotaract General Body", "The Rotaract Club General Body oversees all activities and events.", 2018, "Community Service Day, International Conference, Fundraiser", 35000.00, "Charity Run, Global Outreach Program", "Apply through the Rotaract club website or visit during club hours"),
        ("Rotaract Community Services", "The Rotaract Community Services team focuses on local community service projects.", 2019, "Beach Cleanup, Food Drive", 15000.00, "Community Health Fair", "Join through the Rotaract website or contact community@rotaract.org"),
        ("Rotaract Club Services", "The Rotaract Club Services team manages internal club events and member engagement.", 2018, "Member Socials, Team Building Activities", 10000.00, "Member Retreat", "Join through the Rotaract website or contact clubservices@rotaract.org"),
        ("Rotaract International Services", "The Rotaract International Services team coordinates international service projects.", 2020, "Global Volunteering Program, Cultural Exchange", 20000.00, "International Summit", "Apply through the Rotaract website or email international@rotaract.org"),
        ("Rotaract PR", "The Rotaract PR team handles public relations and communication.", 2019, "Press Releases, Media Relations", 13000.00, "PR Training Session", "Visit the Rotaract office or email pr@rotaract.org"),
        ("Rotaract Marketing", "The Rotaract Marketing team promotes events and activities.", 2018, "Social Media Campaigns, Event Promotions", 15000.00, "Marketing Workshop", "Visit the Rotaract office or email marketing@rotaract.org"),
        ("Rotaract Editorial", "The Rotaract Editorial team manages all publications and written content.", 2019, "Monthly Newsletter, Blog", 10000.00, "Magazine Launch", "Visit the Rotaract office or email editorial@rotaract.org")
    ]
}

# Insert data into each table
for table, data in clubs_data.items():
    cursor.executemany(f'''
        INSERT INTO {table} (NAME, DESCRIPTION, YEAR_INAUGURATED, PAST_EVENTS, BUDGET, UPCOMING_EVENTS, HOW_TO_ENROLL)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', data)

# Display all records from each table
for table in tables.keys():
    print(f"The inserted records in {table} are:")
    data = cursor.execute(f'''SELECT * FROM {table}''')
    for row in data:
        print(row)
    print()

# Commit changes in the database
connection.commit()

# Close the connection
connection.close()
