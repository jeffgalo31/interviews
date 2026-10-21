"""Text transcriptions of every HackerRank SQL image, keyed by the path after hr-challenge-images/."""

def t(header, rows, caption=None):
    out = ([f"*{caption}*", ""] if caption else []) + ["| " + " | ".join(header) + " |", "|" + "---|" * len(header)]
    out += ["| " + " | ".join(str(c) for c in r) + " |" for r in rows]
    return "\n".join(out)

def schema(rows, caption=None):
    return t(["Column", "Type"], rows, caption)

EMP_ROWS = [(12228, "Rose", 15, 1968), (33645, "Angela", 1, 3443), (45692, "Frank", 17, 1608), (56118, "Patrick", 7, 1345),
            (59725, "Lisa", 11, 2330), (74197, "Kimberly", 16, 4372), (78454, "Bonnie", 8, 1771), (83565, "Michael", 6, 2017),
            (98607, "Todd", 5, 3396), (99989, "Joe", 9, 3573)]
OCC_ROWS = [("Samantha", "Doctor"), ("Julia", "Actor"), ("Maria", "Actor"), ("Meera", "Singer"), ("Ashely", "Professor"),
            ("Ketty", "Professor"), ("Christeen", "Professor"), ("Jane", "Actor"), ("Jenny", "Doctor"), ("Priya", "Singer")]

IMG = {
    # shared schemas
    "8137/1449729804-f21d187d0f-CITY.jpg": schema([("ID", "NUMBER"), ("NAME", "VARCHAR2(17)"), ("COUNTRYCODE", "VARCHAR2(3)"),
                                                   ("DISTRICT", "VARCHAR2(20)"), ("POPULATION", "NUMBER")], "CITY").replace("| Column | Type |", "| Field | Type |"),
    "9336/1449345840-5f0a551030-Station.jpg": schema([("ID", "NUMBER"), ("CITY", "VARCHAR2(21)"), ("STATE", "VARCHAR2(2)"),
                                                      ("LAT_N", "NUMBER"), ("LONG_W", "NUMBER")], "STATION").replace("| Column | Type |", "| Field | Type |"),
    "8342/1449769013-e54ce90480-Country.jpg": schema([("CODE", "VARCHAR2(3)"), ("NAME", "VARCHAR2(44)"), ("CONTINENT", "VARCHAR2(13)"),
                                                      ("REGION", "VARCHAR2(25)"), ("SURFACEAREA", "NUMBER"), ("INDEPYEAR", "VARCHAR2(5)"),
                                                      ("POPULATION", "NUMBER"), ("LIFEEXPECTANCY", "VARCHAR2(4)"), ("GNP", "NUMBER"),
                                                      ("GNPOLD", "VARCHAR2(9)"), ("LOCALNAME", "VARCHAR2(44)"), ("GOVERNMENTFORM", "VARCHAR2(44)"),
                                                      ("HEADOFSTATE", "VARCHAR2(32)"), ("CAPITAL", "VARCHAR2(4)"), ("CODE2", "VARCHAR2(2)")],
                                                     "COUNTRY").replace("| Column | Type |", "| Field | Type |"),
    # Employee
    "19629/1458557872-4396838885-ScreenShot2016-03-21at4.27.13PM.png": schema([("employee_id", "Integer"), ("name", "String"), ("months", "Integer"), ("salary", "Integer")]),
    "19629/1458558202-9a8721e44b-ScreenShot2016-03-21at4.32.59PM.png": t(["employee_id", "name", "months", "salary"], EMP_ROWS),
    "19630/1458558612-af3da3ceb7-ScreenShot2016-03-21at4.32.59PM.png": t(["employee_id", "name", "months", "salary"], EMP_ROWS),
    "19631/1458559098-23bf583125-ScreenShot2016-03-21at4.32.59PM.png": t(["employee_id", "name", "months", "salary"], EMP_ROWS),
    "19631/1458559218-9f37585c7a-ScreenShot2016-03-21at4.49.23PM.png": t(["employee_id", "name", "months", "salary", "earnings"],
                                                                           [r + (r[2] * r[3],) for r in EMP_ROWS]),
    # Students (Higher Than 75 Marks)
    "12896/1443815243-94b941f556-1.png": schema([("ID", "Integer"), ("Name", "String"), ("Marks", "Integer")]),
    "12896/1443815209-cf4b260993-2.png": t(["ID", "Name", "Marks"], [(1, "Ashley", 81), (2, "Samantha", 75), (4, "Julia", 76), (3, "Belvet", 84)]),
    # Triangles
    "12887/1443815629-ac2a843fb7-1.png": schema([("A", "Integer"), ("B", "Integer"), ("C", "Integer")]),
    "12887/1443815827-cbfc1ca12b-2.png": t(["A", "B", "C"], [(20, 20, 23), (20, 20, 20), (20, 21, 22), (13, 14, 30)]),
    # Occupations / The PADS
    "12889/1443816414-2a465532e7-1.png": schema([("Name", "String"), ("Occupation", "String")]),
    "12889/1443816608-0b4d01d157-2.png": t(["Name", "Occupation"], OCC_ROWS),
    "12890/1443817648-1b2b8add45-2.png": t(["Name", "Occupation"], OCC_ROWS),
    # The Blunder
    "12893/1443817108-adc2235c81-1.png": schema([("ID", "Integer"), ("Name", "String"), ("Salary", "Integer")]),
    "12893/1443817161-299cc6eb7f-2.png": t(["ID", "Name", "Salary"], [(1, "Kristeen", 1420), (2, "Ashley", 2006), (3, "Julia", 2210), (4, "Maria", 3000)]),
    "12893/1443817229-eb00d44a3b-3.png": t(["ID", "Name", "Salary"], [(1, "Kristeen", 142), (2, "Ashley", 26), (3, "Julia", 221), (4, "Maria", 3)]),
    # The Report
    "12891/1443818166-a5c852caa0-1.png": schema([("ID", "Integer"), ("Name", "String"), ("Marks", "Integer")]),
    "12891/1443818137-69b76d805c-2.png": t(["Grade", "Min_Mark", "Max_Mark"], [(g, (g - 1) * 10, g * 10 - 1 if g < 10 else 100) for g in range(1, 11)]),
    "12891/1443818093-b79f376ec1-3.png": t(["ID", "Name", "Marks"], [(1, "Julia", 88), (2, "Samantha", 68), (3, "Maria", 99), (4, "Scarlet", 78), (5, "Ashley", 63), (6, "Jane", 81)]),
    "12891/1443818026-0b3af8db30-4.png": t(["ID", "Name", "Marks", "Grade"], [(1, "Julia", 88, 9), (2, "Samantha", 68, 7), (3, "Maria", 99, 10),
                                                                            (4, "Scarlet", 78, 8), (5, "Ashley", 63, 7), (6, "Jane", 81, 9)]),
    # Placements
    "12895/1443820186-2a9b4939a8-1.png": "\n\n".join([schema([("ID", "Integer"), ("Name", "String")], "Students"),
                                                       schema([("ID", "Integer"), ("Friend_ID", "Integer")], "Friends"),
                                                       schema([("ID", "Integer"), ("Salary", "Float")], "Packages")]),
    "12895/1443820079-9bd1e231b1-2_1.png": t(["ID", "Name"], [(1, "Ashley"), (2, "Samantha"), (3, "Julia"), (4, "Scarlet")], "Students"),
    "12895/1443820100-adb691b2f5-2_2.png": t(["ID", "Friend_ID"], [(1, 2), (2, 3), (3, 4), (4, 1)], "Friends") + "\n\n" +
                                           t(["ID", "Salary"], [(1, "15.20"), (2, "10.06"), (3, "11.55"), (4, "12.12")], "Packages"),
    "12895/1443819966-c37c146d27-3.png": t(["ID", "Name", "Salary", "Friend ID", "Friend Salary"],
                                           [(1, "Ashley", "15.20", 2, "10.06"), (2, "Samantha", "10.06", 3, "11.55"),
                                            (3, "Julia", "11.55", 4, "12.12"), (4, "Scarlet", "12.12", 1, "15.20")]),
    # SQL Project Planning
    "12894/1443819551-639948acc0-1.png": schema([("Task_ID", "Integer"), ("Start_Date", "Date"), ("End_Date", "Date")]),
    "12894/1443819440-1c40e943a1-2.png": t(["Task_ID", "Start_Date", "End_Date"],
                                           [(1, "2015-10-01", "2015-10-02"), (2, "2015-10-02", "2015-10-03"), (3, "2015-10-03", "2015-10-04"),
                                            (4, "2015-10-13", "2015-10-14"), (5, "2015-10-14", "2015-10-15"), (6, "2015-10-28", "2015-10-29"),
                                            (7, "2015-10-30", "2015-10-31")]),
    # Symmetric Pairs
    "12892/1443818798-51909e977d-1.png": schema([("X", "Integer"), ("Y", "Integer")]),
    "12892/1443818693-b384c24e35-2.png": t(["X", "Y"], [(20, 20), (20, 20), (20, 21), (23, 22), (22, 23), (21, 20)]),
    # Binary Tree Nodes
    "12888/1443818507-5095ab9853-1.png": schema([("N", "Integer"), ("P", "Integer")]),
    "12888/1443818467-30644673f6-2.png": t(["N", "P"], [(1, 2), (3, 2), (6, 8), (9, 8), (2, 5), (8, 5), (5, "null")]),
    "12888/1443773633-f9e6fd314e-simply_sql_bst.png": "```\n        5\n      /   \\\n     2     8\n    / \\   / \\\n   1   3 6   9\n```",
    # New Companies
    "19505/1458531031-249df3ae87-ScreenShot2016-03-21at8.59.56AM.png": "```\nFounder\n   ↓\nLead Manager\n   ↓\nSenior Manager\n   ↓\nManager\n   ↓\nEmployee\n```",
    "19505/1458531125-deb0a57ae1-ScreenShot2016-03-21at8.50.04AM.png": schema([("company_code", "String"), ("founder", "String")]),
    "19505/1458534960-2c6d764e3c-ScreenShot2016-03-21at8.50.12AM.png": schema([("lead_manager_code", "String"), ("company_code", "String")]),
    "19505/1458534973-6548194998-ScreenShot2016-03-21at8.50.21AM.png": schema([("senior_manager_code", "String"), ("lead_manager_code", "String"), ("company_code", "String")]),
    "19505/1458534988-7fc0af46ce-ScreenShot2016-03-21at8.50.29AM.png": schema([("manager_code", "String"), ("senior_manager_code", "String"),
                                                                                ("lead_manager_code", "String"), ("company_code", "String")]),
    "19505/1458535002-d47f63cbb4-ScreenShot2016-03-21at8.50.41AM.png": schema([("employee_code", "String"), ("manager_code", "String"), ("senior_manager_code", "String"),
                                                                                ("lead_manager_code", "String"), ("company_code", "String")]),
    "19505/1458535049-2a207c44b3-ScreenShot2016-03-21at8.50.52AM.png": t(["company_code", "founder"], [("C1", "Monika"), ("C2", "Samantha")]),
    "19505/1458535073-919107f639-ScreenShot2016-03-21at8.51.03AM.png": t(["lead_manager_code", "company_code"], [("LM1", "C1"), ("LM2", "C2")]),
    "19505/1458535111-b1c48335b3-ScreenShot2016-03-21at8.51.15AM.png": t(["senior_manager_code", "lead_manager_code", "company_code"],
                                                                           [("SM1", "LM1", "C1"), ("SM2", "LM1", "C1"), ("SM3", "LM2", "C2")]),
    "19505/1458535122-888f4bf340-ScreenShot2016-03-21at8.51.26AM.png": t(["manager_code", "senior_manager_code", "lead_manager_code", "company_code"],
                                                                           [("M1", "SM1", "LM1", "C1"), ("M2", "SM3", "LM2", "C2"), ("M3", "SM3", "LM2", "C2")]),
    "19505/1458535134-878767e0d9-ScreenShot2016-03-21at8.51.52AM.png": t(["employee_code", "manager_code", "senior_manager_code", "lead_manager_code", "company_code"],
                                                                           [("E1", "M1", "SM1", "LM1", "C1"), ("E2", "M1", "SM1", "LM1", "C1"),
                                                                            ("E3", "M2", "SM3", "LM2", "C2"), ("E4", "M3", "SM3", "LM2", "C2")]),
}

HACK_SCHEMA = schema([("hacker_id", "Integer"), ("name", "String")])
# Challenges
CH0_H = [(5077, "Rose"), (21283, "Angela"), (62743, "Frank"), (88255, "Patrick"), (96196, "Lisa")]
CH0_C = [(61654, 5077), (58302, 21283), (40587, 88255), (29477, 5077), (1220, 21283), (69514, 21283), (46561, 62743), (58077, 62743),
         (18483, 88255), (76766, 21283), (52382, 5077), (74467, 21283), (33625, 96196), (26053, 88255), (42665, 62743), (12859, 62743),
         (70094, 21283), (34599, 88255), (54680, 88255), (61881, 5077)]
CH1_H = [(12299, "Rose"), (34856, "Angela"), (79345, "Frank"), (80491, "Patrick"), (81041, "Lisa")]
CH1_C = [(63963, 81041), (63117, 79345), (28225, 34856), (21989, 12299), (4653, 12299), (70070, 79345), (36905, 34856), (61136, 80491),
         (17234, 12299), (80308, 79345), (40510, 34856), (79820, 80491), (22720, 12299), (21394, 12299), (36261, 34856), (15334, 12299),
         (71435, 79345), (23157, 34856), (54102, 34856), (69065, 80491)]
IMG.update({
    "19506/1458521004-cb4c077dd3-ScreenShot2016-03-21at6.06.54AM.png": HACK_SCHEMA,
    "19506/1458521079-549341d9ec-ScreenShot2016-03-21at6.07.03AM.png": schema([("challenge_id", "Integer"), ("hacker_id", "Integer")]),
    "19506/1458521384-34c6866dae-ScreenShot2016-03-21at6.07.15AM.png": t(["hacker_id", "name"], CH0_H),
    "19506/1458521410-befa8e1cd9-ScreenShot2016-03-21at6.07.25AM.png": t(["challenge_id", "hacker_id"], CH0_C),
    "19506/1458521469-87036deea3-ScreenShot2016-03-21at6.07.48AM.png": t(["hacker_id", "name"], CH1_H),
    "19506/1458521490-358215cf0b-ScreenShot2016-03-21at6.07.58AM.png": t(["challenge_id", "hacker_id"], CH1_C),
})
# Contest Leaderboard
CL_H = [(4071, "Rose"), (4806, "Angela"), (26071, "Frank"), (49438, "Patrick"), (74842, "Lisa"), (80305, "Kimberly"),
        (84072, "Bonnie"), (87868, "Michael"), (92118, "Todd"), (95895, "Joe")]
CL_S = [(67194, 74842, 63132, 76), (64479, 74842, 19797, 98), (40742, 26071, 49593, 20), (17513, 4806, 49593, 32),
        (69846, 80305, 19797, 19), (41002, 26071, 89343, 36), (52826, 49438, 49593, 9), (31093, 26071, 19797, 2),
        (81614, 84072, 49593, 100), (44829, 26071, 89343, 17), (75147, 80305, 49593, 48), (14115, 4806, 49593, 76),
        (6943, 4071, 19797, 95), (12855, 4806, 25917, 13), (73343, 80305, 49593, 42), (84264, 84072, 63132, 0),
        (9951, 4071, 49593, 43), (45104, 49438, 25917, 34), (53795, 74842, 19797, 5), (26363, 26071, 19797, 29),
        (10063, 4071, 49593, 96)]
SUB_SCHEMA = schema([("submission_id", "Integer"), ("hacker_id", "Integer"), ("challenge_id", "Integer"), ("score", "Integer")])
IMG.update({
    "19503/1458522826-a9ddd28469-ScreenShot2016-03-21at6.40.27AM.png": HACK_SCHEMA,
    "19503/1458523022-771511df90-ScreenShot2016-03-21at6.40.37AM.png": SUB_SCHEMA,
    "19503/1458523374-7ecc39010f-ScreenShot2016-03-21at6.51.56AM.png": t(["hacker_id", "name"], CL_H),
    "19503/1458523388-0896218137-ScreenShot2016-03-21at6.51.45AM.png": t(["submission_id", "hacker_id", "challenge_id", "score"], CL_S),
})
# Ollivander's Inventory
OL_W = [(1, 4, 3688, 8), (2, 3, 9365, 3), (3, 3, 7187, 10), (4, 3, 734, 8), (5, 1, 6020, 2), (6, 2, 6773, 7), (7, 3, 9873, 9),
        (8, 3, 7721, 7), (9, 1, 1647, 10), (10, 4, 504, 5), (11, 2, 7587, 5), (12, 5, 9897, 10), (13, 3, 4651, 8), (14, 2, 5408, 1),
        (15, 2, 6018, 7), (16, 4, 7710, 5), (17, 2, 8798, 7), (18, 2, 3312, 3), (19, 4, 7651, 6), (20, 5, 5689, 3)]
OL_P = [(1, 45, 0), (2, 40, 0), (3, 4, 1), (4, 20, 0), (5, 17, 0)]
IMG.update({
    "19502/1458538092-b2a8163a74-ScreenShot2016-03-08at12.13.39AM.png": schema([("id", "Integer"), ("code", "Integer"), ("coins_needed", "Integer"), ("power", "Integer")]),
    "19502/1458538221-18c4092b7d-ScreenShot2016-03-08at12.13.53AM.png": schema([("code", "Integer"), ("age", "Integer"), ("is_evil", "Integer")]),
    "19502/1458538559-51bf29644e-ScreenShot2016-03-21at10.34.41AM.png": t(["id", "code", "coins_needed", "power"], OL_W),
    "19502/1458538583-fd514566f9-ScreenShot2016-03-21at10.34.28AM.png": t(["code", "age", "is_evil"], OL_P),
})
# Top Competitors
TC_H = [(5580, "Rose"), (8439, "Angela"), (27205, "Frank"), (52243, "Patrick"), (52348, "Lisa"), (57645, "Kimberly"),
        (77726, "Bonnie"), (83082, "Michael"), (86870, "Todd"), (90411, "Joe")]
TC_D = [(1, 20), (2, 30), (3, 40), (4, 60), (5, 80), (6, 100), (7, 120)]
TC_C = [(4810, 77726, 4), (21089, 27205, 1), (36566, 5580, 7), (66730, 52243, 6), (71055, 52243, 2)]
TC_S = [(68628, 77726, 36566, 30), (65300, 77726, 21089, 10), (40326, 52243, 36566, 77), (8941, 27205, 4810, 4),
        (83554, 77726, 66730, 30), (43353, 52243, 66730, 0), (55385, 52348, 71055, 20), (39784, 27205, 71055, 23),
        (94613, 86870, 71055, 30), (45788, 52348, 36566, 0), (93058, 86870, 36566, 30), (7344, 8439, 66730, 92),
        (2721, 8439, 4810, 36), (523, 5580, 71055, 4), (49105, 52348, 66730, 0), (55877, 57645, 66730, 80),
        (38355, 27205, 66730, 35), (3924, 8439, 36566, 80), (97397, 90411, 66730, 100), (84162, 83082, 4810, 40),
        (97431, 90411, 71055, 30)]
IMG.update({
    "19504/1458526776-67667350b4-ScreenShot2016-03-21at7.45.59AM.png": HACK_SCHEMA,
    "19504/1458526915-57eb75d9a2-ScreenShot2016-03-21at7.46.09AM.png": schema([("difficulty_level", "Integer"), ("score", "Integer")]),
    "19504/1458527032-f9ca650442-ScreenShot2016-03-21at7.46.17AM.png": schema([("challenge_id", "Integer"), ("hacker_id", "Integer"), ("difficulty_level", "Integer")]),
    "19504/1458527077-298f8e922a-ScreenShot2016-03-21at7.46.29AM.png": SUB_SCHEMA,
    "19504/1458527241-6922b4ad87-ScreenShot2016-03-21at7.47.02AM.png": t(["hacker_id", "name"], TC_H),
    "19504/1458527265-7ad6852a13-ScreenShot2016-03-21at7.46.50AM.png": t(["difficulty_level", "score"], TC_D),
    "19504/1458527285-01e95eb6ec-ScreenShot2016-03-21at7.46.40AM.png": t(["challenge_id", "hacker_id", "difficulty_level"], TC_C),
    "19504/1458527812-479a74b99f-ScreenShot2016-03-21at8.06.05AM.png": t(["submission_id", "hacker_id", "challenge_id", "score"], TC_S),
})
# Interviews
IV_CT = [(66406, 17973, "Rose"), (66556, 79153, "Angela"), (94828, 80275, "Frank")]
IV_CO = [(11219, 66406), (32473, 66556), (56685, 94828)]
IV_CH = [(18765, 11219), (47127, 11219), (60292, 32473), (72974, 56685)]
IV_V = [(47127, 26, 19), (47127, 15, 14), (18765, 43, 10), (18765, 72, 13), (75516, 35, 17), (60292, 11, 10), (72974, 41, 15), (75516, 75, 11)]
IV_S = [(75516, 34, 12), (47127, 27, 10), (47127, 56, 18), (75516, 74, 12), (75516, 83, 8), (72974, 68, 24), (72974, 82, 14), (47127, 28, 11)]
IMG.update({
    "19596/1458517426-e017c3460e-ScreenShot2016-03-21at4.57.47AM.png": schema([("contest_id", "Integer"), ("hacker_id", "Integer"), ("name", "String")]),
    "19596/1458517503-fd4aa63111-ScreenShot2016-03-21at4.57.56AM.png": schema([("college_id", "Integer"), ("contest_id", "Integer")]),
    "19596/1458517661-a642f750ce-ScreenShot2016-03-21at4.58.04AM.png": schema([("challenge_id", "Integer"), ("college_id", "Integer")]),
    "19596/1458517983-b4302286a8-ScreenShot2016-03-21at4.58.15AM.png": schema([("challenge_id", "Integer"), ("total_views", "Integer"), ("total_unique_views", "Integer")]),
    "19596/1458518090-80983c916a-ScreenShot2016-03-21at4.58.27AM.png": schema([("challenge_id", "Integer"), ("total_submissions", "Integer"), ("total_accepted_submissions", "Integer")]),
    "19596/1458519044-d788f8a6ee-ScreenShot2016-03-21at4.58.39AM.png": t(["contest_id", "hacker_id", "name"], IV_CT),
    "19596/1458519098-912836d6ac-ScreenShot2016-03-21at4.59.22AM.png": t(["college_id", "contest_id"], IV_CO),
    "19596/1458519120-c531743caf-ScreenShot2016-03-21at4.59.32AM.png": t(["challenge_id", "college_id"], IV_CH),
    "19596/1458519152-107a67866b-ScreenShot2016-03-21at4.59.43AM.png": t(["challenge_id", "total_views", "total_unique_views"], IV_V),
    "19596/1458519173-091aba871a-ScreenShot2016-03-21at4.59.55AM.png": t(["challenge_id", "total_submissions", "total_accepted_submissions"], IV_S),
})
# 15 Days of Learning SQL
FD_H = [(15758, "Rose"), (20703, "Angela"), (36396, "Frank"), (38289, "Patrick"), (44065, "Lisa"), (53473, "Kimberly"),
        (62529, "Bonnie"), (79722, "Michael")]
FD_S = [("2016-03-01", 8494, 20703, 0), ("2016-03-01", 22403, 53473, 15), ("2016-03-01", 23965, 79722, 60), ("2016-03-01", 30173, 36396, 70),
        ("2016-03-02", 34928, 20703, 0), ("2016-03-02", 38740, 15758, 60), ("2016-03-02", 42769, 79722, 25), ("2016-03-02", 44364, 79722, 60),
        ("2016-03-03", 45440, 20703, 0), ("2016-03-03", 49050, 36396, 70), ("2016-03-03", 50273, 79722, 5),
        ("2016-03-04", 50344, 20703, 0), ("2016-03-04", 51360, 44065, 90), ("2016-03-04", 54404, 53473, 65), ("2016-03-04", 61533, 79722, 45),
        ("2016-03-05", 72852, 20703, 0), ("2016-03-05", 74546, 38289, 0), ("2016-03-05", 76487, 62529, 0), ("2016-03-05", 82439, 36396, 10),
        ("2016-03-05", 90006, 36396, 40), ("2016-03-06", 90404, 20703, 0)]
IMG.update({
    "19597/1458511164-12adec3b8b-ScreenShot2016-03-21at3.26.47AM.png": HACK_SCHEMA,
    "19597/1458511251-0b534030b9-ScreenShot2016-03-21at3.26.56AM.png": schema([("submission_date", "Date"), ("submission_id", "Integer"), ("hacker_id", "Integer"), ("score", "Integer")]),
    "19597/1458511957-814a2c7bf2-ScreenShot2016-03-21at3.27.06AM.png": t(["hacker_id", "name"], FD_H),
    "19597/1458512015-ff6a708164-ScreenShot2016-03-21at3.27.21AM.png": t(["submission_date", "submission_id", "hacker_id", "score"], FD_S),
})

def sql_values(rows):
    def lit(v):
        return "NULL" if v is None else (f"'{v}'" if isinstance(v, str) else str(v))
    return ",\n".join("    (" + ", ".join(lit(v) for v in r) + ")" for r in rows) + ";"

# Explanations whose numbers were formulas on HackerRank: HackerRank's wording with the numbers filled in.
def _wands(age, code):
    rows = [w for w in OL_W if w[1] == code]
    mins = {}
    for w in rows:
        mins[w[3]] = min(mins.get(w[3], 10**9), w[2])
    return (t(["id", "age", "coins_needed", "power"], [(w[0], age, w[2], w[3]) for w in sorted(rows, key=lambda w: (w[3], w[2]))]) + "\n\n" +
            "\n".join(f"- The minimum number of galleons needed for wand(age = {age}, power = {p}) = {c}" for p, c in sorted(mins.items())))

EXPLAIN = {
    "weather-observation-station-5": "When ordered alphabetically, the **CITY** names are listed as **ABC, DEF, PQRS,** and **WXY**, with lengths 3, 3, 4, and 3. "
        "The longest name is **PQRS**, but there are 3 options for shortest named city. Choose **ABC**, because it comes first alphabetically.\n\n"
        "**Note**\n\nYou can write two separate queries to get the desired output. It need not be a single query.",
    "more-than-75-marks": "Only Ashley, Julia, and Belvet have Marks > 75. If you look at the last three characters of each of their names, "
        "there are no duplicates and 'ley' < 'lia' < 'vet'.",
    "salary-of-employees": "Angela has been an employee for 1 month and earns $3443 per month.\n\n"
        "Michael has been an employee for 6 months and earns $2017 per month.\n\n"
        "Todd has been an employee for 5 months and earns $3396 per month.\n\n"
        "Joe has been an employee for 9 months and earns $3573 per month.\n\nWe order our output by ascending employee_id.",
    "what-type-of-triangle": "Values in the tuple (20, 20, 23) form an Isosceles triangle, because A ≡ B.\n\n"
        "Values in the tuple (20, 20, 20) form an Equilateral triangle, because A ≡ B ≡ C.\n\n"
        "Values in the tuple (20, 21, 22) form a Scalene triangle, because A ≠ B ≠ C.\n\n"
        "Values in the tuple (13, 14, 30) cannot form a triangle because the combined value of sides A and B is not larger than that of side C.",
    "the-blunder": "The table below shows the salaries without zeros as they were entered by Samantha:\n\n"
        + IMG["12893/1443817229-eb00d44a3b-3.png"] + "\n\n"
        "Samantha computes an average salary of 98.00. The actual average salary is 2159.00.\n\n"
        "The resulting error between the two calculations is 2159.00 − 98.00 = 2061.00. Since it is equal to the integer 2061, it does not get rounded up.",
    "earnings-of-employees": "The table and earnings data is depicted in the following diagram:\n\n"
        + IMG["19631/1458559218-9f37585c7a-ScreenShot2016-03-21at4.49.23PM.png"] + "\n\n"
        "The maximum earnings value is 69952. The only employee with earnings = 69952 is Kimberly, so we print the maximum earnings value (69952) "
        "and a count of the number of employees who have earned $69952 (which is 1) as two space-separated values.",
    "full-score": "Hacker 86870 got a score of 30 for challenge 71055 with a difficulty level of 2, so 86870 earned a full score for this challenge.\n\n"
        "Hacker 90411 got a score of 30 for challenge 71055 with a difficulty level of 2, so 90411 earned a full score for this challenge.\n\n"
        "Hacker 90411 got a score of 100 for challenge 66730 with a difficulty level of 6, so 90411 earned a full score for this challenge.\n\n"
        "Only hacker 90411 managed to earn a full score for more than one challenge, so we print the their hacker_id and name as 2 space-separated values.",
    "harry-potter-and-wands": "The data for wands of age 45 (code 1):\n\n" + _wands(45, 1) +
        "\n\nThe data for wands of age 40 (code 2):\n\n" + _wands(40, 2) +
        "\n\nThe data for wands of age 20 (code 4):\n\n" + _wands(20, 4) +
        "\n\nThe data for wands of age 17 (code 5):\n\n" + _wands(17, 5),
    "contest-leaderboard": "Hacker 4071 submitted solutions for challenges 19797 and 49593, so the total score = 95 + max(43, 96) = 191.\n\n"
        "Hacker 74842 submitted solutions for challenges 19797 and 63132, so the total score = max(98, 5) + 76 = 174.\n\n"
        "Hacker 84072 submitted solutions for challenges 49593 and 63132, so the total score = 100 + 0 = 100.\n\n"
        "The total scores for hackers 4806, 26071, 80305, and 49438 can be similarly calculated.",
    "interviews": "The contest 66406 is used in the college 11219. In this college 11219, challenges 18765 and 47127 are asked, so from the view and submission stats:\n\n"
        "- Sum of total submissions = 27 + 56 + 28 = 111\n- Sum of total accepted submissions = 10 + 18 + 11 = 39\n"
        "- Sum of total views = 43 + 72 + 26 + 15 = 156\n- Sum of total unique views = 10 + 13 + 19 + 14 = 56\n\n"
        "Similarly, we can find the sums for contests 66556 and 94828.",
    "15-days-of-learning-sql": "On March 01, 2016 hackers 20703, 36396, 53473, and 79722 made submissions. There are 4 unique hackers who made at least one submission each day. "
        "As each hacker made one submission, 20703 is considered to be the hacker who made maximum number of submissions on this day. The name of the hacker is Angela.\n\n"
        "On March 02, 2016 hackers 15758, 20703, and 79722 made submissions. Now 20703 and 79722 were the only ones to submit every day, so there are 2 unique hackers "
        "who made at least one submission each day. 79722 made 2 submissions, and name of the hacker is Michael.\n\n"
        "On March 03, 2016 hackers 20703, 36396, and 79722 made submissions. Now 20703 and 79722 were the only ones, so there are 2 unique hackers who made at least "
        "one submission each day. As each hacker made one submission so 20703 is considered to be the hacker who made maximum number of submissions on this day. "
        "The name of the hacker is Angela.\n\n"
        "On March 04, 2016 hackers 20703, 44065, 53473, and 79722 made submissions. Now 20703 and 79722 only submitted each day, so there are 2 unique hackers who "
        "made at least one submission each day. As each hacker made one submission so 20703 is considered to be the hacker who made maximum number of submissions "
        "on this day. The name of the hacker is Angela.\n\n"
        "On March 05, 2016 hackers 20703, 36396, 38289 and 62529 made submissions. Now 20703 only submitted each day, so there is only 1 unique hacker who made at "
        "least one submission each day. 36396 made 2 submissions and name of the hacker is Frank.\n\n"
        "On March 06, 2016 only 20703 made submission, so there is only 1 unique hacker who made at least one submission each day. 20703 made 1 submission and name "
        "of the hacker is Angela.",
}
