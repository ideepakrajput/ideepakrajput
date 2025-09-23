#!/usr/bin/env python3
"""
Convert the test paper to HTML format which can be opened in Word
"""

html_content = """<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Class 6 Mathematics Test Paper</title>
    <style>
        body {
            font-family: 'Times New Roman', Times, serif;
            font-size: 12pt;
            line-height: 1.5;
            margin: 1in;
        }
        h1 {
            text-align: center;
            font-size: 18pt;
            margin-bottom: 10pt;
        }
        h2 {
            font-size: 14pt;
            margin-top: 20pt;
            margin-bottom: 10pt;
        }
        h3 {
            font-size: 12pt;
            font-weight: bold;
            margin-top: 15pt;
            margin-bottom: 10pt;
        }
        .subtitle {
            text-align: center;
            font-weight: bold;
            margin-bottom: 20pt;
        }
        .time-marks {
            text-align: center;
            font-weight: bold;
            margin-bottom: 20pt;
        }
        .question {
            margin-bottom: 15pt;
        }
        .question-number {
            font-weight: bold;
        }
        .marks {
            font-weight: bold;
        }
        .options {
            margin-left: 20pt;
            margin-top: 5pt;
        }
        table {
            border-collapse: collapse;
            margin: 10pt 0;
        }
        table, th, td {
            border: 1px solid black;
            padding: 5pt;
        }
        .divider {
            border-bottom: 1px solid black;
            margin: 20pt 0;
        }
        .center {
            text-align: center;
        }
        ol, ul {
            margin-left: 20pt;
        }
    </style>
</head>
<body>
    <h1>CLASS 6 MATHEMATICS TEST PAPER</h1>
    <p class="subtitle">Session: 2025-26 | Based on NCERT Ganita Prakash</p>
    <p class="time-marks">Time: 1.5 Hours &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Maximum Marks: 50</p>
    
    <div class="divider"></div>
    
    <h3>GENERAL INSTRUCTIONS:</h3>
    <ol>
        <li>All questions are compulsory.</li>
        <li>This question paper contains 20 questions divided into four sections A, B, C and D.</li>
        <li>Section A contains 10 questions of 1 mark each (MCQs and Very Short Answer).</li>
        <li>Section B contains 5 questions of 2 marks each (Short Answer).</li>
        <li>Section C contains 3 questions of 3 marks each (Short Answer).</li>
        <li>Section D contains 2 questions of 5 marks each (Long Answer).</li>
        <li>Use of calculator is not allowed.</li>
        <li>Write neat and legible answers.</li>
    </ol>
    
    <div class="divider"></div>
    
    <h2>SECTION A: Multiple Choice Questions & Very Short Answer (1 mark each)</h2>
    
    <div class="question">
        <span class="question-number">Q1.</span> Which of the following is a prime number? <span class="marks">(1 mark)</span>
        <div class="options">
            (a) 91 &nbsp;&nbsp;&nbsp; (b) 97 &nbsp;&nbsp;&nbsp; (c) 93 &nbsp;&nbsp;&nbsp; (d) 95
        </div>
    </div>
    
    <div class="question">
        <span class="question-number">Q2.</span> The angle between two perpendicular lines is: <span class="marks">(1 mark)</span>
        <div class="options">
            (a) 45° &nbsp;&nbsp;&nbsp; (b) 60° &nbsp;&nbsp;&nbsp; (c) 90° &nbsp;&nbsp;&nbsp; (d) 180°
        </div>
    </div>
    
    <div class="question">
        <span class="question-number">Q3.</span> Complete the pattern: 2, 5, 10, 17, 26, ___ <span class="marks">(1 mark)</span>
    </div>
    
    <div class="question">
        <span class="question-number">Q4.</span> Write the next two terms in the pattern: 1, 4, 9, 16, ___, ___ <span class="marks">(1 mark)</span>
    </div>
    
    <div class="question">
        <span class="question-number">Q5.</span> The mode of the data set {3, 5, 7, 5, 9, 5, 3, 7} is: <span class="marks">(1 mark)</span>
        <div class="options">
            (a) 3 &nbsp;&nbsp;&nbsp; (b) 5 &nbsp;&nbsp;&nbsp; (c) 7 &nbsp;&nbsp;&nbsp; (d) 9
        </div>
    </div>
    
    <div class="question">
        <span class="question-number">Q6.</span> How many degrees are there in a straight angle? <span class="marks">(1 mark)</span>
    </div>
    
    <div class="question">
        <span class="question-number">Q7.</span> Express 48 as a product of prime factors. <span class="marks">(1 mark)</span>
    </div>
    
    <div class="question">
        <span class="question-number">Q8.</span> If a triangle has angles measuring 50°, 60°, and 70°, what type of triangle is it? <span class="marks">(1 mark)</span>
        <div class="options">
            (a) Right triangle &nbsp;&nbsp;&nbsp; (b) Acute triangle &nbsp;&nbsp;&nbsp; (c) Obtuse triangle &nbsp;&nbsp;&nbsp; (d) Equilateral triangle
        </div>
    </div>
    
    <div class="question">
        <span class="question-number">Q9.</span> The mean of first five natural numbers is _____. <span class="marks">(1 mark)</span>
    </div>
    
    <div class="question">
        <span class="question-number">Q10.</span> State whether True or False: "1 is neither prime nor composite." <span class="marks">(1 mark)</span>
    </div>
    
    <div class="divider"></div>
    
    <h2>SECTION B: Short Answer Questions (2 marks each)</h2>
    
    <div class="question">
        <span class="question-number">Q11.</span> Draw and label the following angles: <span class="marks">(2 marks)</span>
        <div style="margin-left: 20pt; margin-top: 5pt;">
            (a) An acute angle of 45°<br>
            (b) An obtuse angle of 120°
        </div>
    </div>
    
    <div class="question">
        <span class="question-number">Q12.</span> Find the HCF of 36 and 48 using prime factorization method. <span class="marks">(2 marks)</span>
    </div>
    
    <div class="question">
        <span class="question-number">Q13.</span> The following data shows the marks obtained by 10 students in a test: <span class="marks">(2 marks)</span>
        <div style="margin-left: 20pt; margin-top: 5pt;">
            15, 18, 12, 20, 15, 16, 18, 15, 19, 17<br><br>
            Find the mode and median of this data.
        </div>
    </div>
    
    <div class="question">
        <span class="question-number">Q14.</span> Complete the following number patterns and write the rule: <span class="marks">(2 marks)</span>
        <div style="margin-left: 20pt; margin-top: 5pt;">
            (a) 3, 6, 12, 24, ___, ___<br>
            (b) 100, 95, 85, 70, ___, ___
        </div>
    </div>
    
    <div class="question">
        <span class="question-number">Q15.</span> List all prime numbers between 30 and 50. Also find their sum. <span class="marks">(2 marks)</span>
    </div>
    
    <div class="divider"></div>
    
    <h2>SECTION C: Short Answer Questions (3 marks each)</h2>
    
    <div class="question">
        <span class="question-number">Q16.</span> The following bar graph shows the favorite subjects of students in a class: <span class="marks">(3 marks)</span>
        <table style="margin-top: 10pt;">
            <tr>
                <th>Subject</th>
                <th>Number of Students</th>
            </tr>
            <tr>
                <td>Mathematics</td>
                <td>12</td>
            </tr>
            <tr>
                <td>Science</td>
                <td>8</td>
            </tr>
            <tr>
                <td>English</td>
                <td>10</td>
            </tr>
            <tr>
                <td>Hindi</td>
                <td>6</td>
            </tr>
            <tr>
                <td>Social Studies</td>
                <td>4</td>
            </tr>
        </table>
        <div style="margin-top: 10pt;">
            (a) How many students were surveyed in total?<br>
            (b) Which subject is most popular?<br>
            (c) What fraction of students prefer Mathematics?
        </div>
    </div>
    
    <div class="question">
        <span class="question-number">Q17.</span> In the given figure, if angle AOB = 130° and OC bisects angle AOB, find: <span class="marks">(3 marks)</span>
        <div style="margin-left: 20pt; margin-top: 5pt;">
            (a) Angle AOC<br>
            (b) Angle BOC<br>
            (c) What type of angles are AOC and BOC?<br><br>
            [Note: Assume O is the vertex and OA, OB, OC are rays]
        </div>
    </div>
    
    <div class="question">
        <span class="question-number">Q18.</span> A number is divisible by 6. Is it necessary that the number is divisible by 2 and 3? Explain with examples. Also, check whether 258 is divisible by 6. <span class="marks">(3 marks)</span>
    </div>
    
    <div class="divider"></div>
    
    <h2>SECTION D: Long Answer Questions (5 marks each)</h2>
    
    <div class="question">
        <span class="question-number">Q19.</span> Study the following pattern and answer the questions: <span class="marks">(5 marks)</span>
        <div style="margin-left: 20pt; margin-top: 5pt;">
            Pattern 1: •<br>
            Pattern 2: • • •<br>
            Pattern 3: • • • • •<br>
            Pattern 4: • • • • • • •<br><br>
            
            (a) Draw Pattern 5 (1 mark)<br>
            (b) How many dots are in Pattern 6? (1 mark)<br>
            (c) Write a formula for the number of dots in Pattern n (2 marks)<br>
            (d) How many dots will be in Pattern 10? (1 mark)
        </div>
    </div>
    
    <div class="question">
        <span class="question-number">Q20.</span> The following table shows the temperature (in °C) recorded in a city for 7 days: <span class="marks">(5 marks)</span>
        <table style="margin-top: 10pt;">
            <tr>
                <th>Day</th>
                <th>Mon</th>
                <th>Tue</th>
                <th>Wed</th>
                <th>Thu</th>
                <th>Fri</th>
                <th>Sat</th>
                <th>Sun</th>
            </tr>
            <tr>
                <td>Temperature</td>
                <td>28</td>
                <td>30</td>
                <td>32</td>
                <td>29</td>
                <td>31</td>
                <td>33</td>
                <td>30</td>
            </tr>
        </table>
        <div style="margin-top: 10pt;">
            (a) Represent this data using a bar graph (2 marks)<br>
            (b) Calculate the mean temperature for the week (1 mark)<br>
            (c) Find the range of temperatures (1 mark)<br>
            (d) On which day(s) was the temperature equal to the mode? (1 mark)
        </div>
    </div>
    
    <div class="divider"></div>
    
    <h3>MARKING SCHEME SUMMARY:</h3>
    <ul>
        <li>Section A: 10 × 1 = 10 marks</li>
        <li>Section B: 5 × 2 = 10 marks</li>
        <li>Section C: 3 × 3 = 9 marks</li>
        <li>Section D: 2 × 5 = 10 marks</li>
        <li><strong>Total: 50 marks</strong></li>
    </ul>
    
    <div class="divider"></div>
    
    <p class="center"><strong>END OF QUESTION PAPER</strong></p>
    <p class="center"><em>All the best!</em></p>
</body>
</html>"""

# Save the HTML file
with open('/workspace/Class_6_Mathematics_Test_Paper.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("HTML file created successfully!")
print("This file can be opened in Microsoft Word:")
print("1. Open Microsoft Word")
print("2. Go to File > Open")
print("3. Select 'Class_6_Mathematics_Test_Paper.html'")
print("4. Word will automatically convert and format it")
print("5. You can then save it as a .docx file")