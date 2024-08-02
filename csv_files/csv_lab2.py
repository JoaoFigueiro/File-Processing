import csv 


class Exam:
    def __init__(self, name): 
        self.name = name
        self.candidates = []
        self.scores = []
        self.grade = []

    def return_candidates(self): 
        return len(set(self.candidates))

    def return_passed(self): 
        return self.grade.count("Pass") 

    def return_failed(self):
        return self.grade.count("Fail") 
    
    def return_best_score(self): 
        if len(self.scores) == 0: 
            best_score = 0
        else: 
            self.scores.sort() 
            best_score = self.scores[-1]

        return best_score

    def return_worst_score(self):
        if len(self.scores) == 0: 
            worst_score = 0
        else: 
            self.scores.sort() 
            worst_score = self.scores[0]

        return worst_score           


def create_new_csv(rows: list[dict]): 
    field_names = [
        "Exam Name",
        "Number of Candidates",
        "Number of Passed Exams",
        "Number of Failed Exams",
        "Best Score",
        "Worst Score"
    ]
    
    with open("report.csv", "w", newline="") as report: 
        writer = csv.DictWriter(report, fieldnames=field_names)
        
        writer.writeheader()
        writer.writerows(rows)

file_name = 'exam_results.csv'

with open(file_name) as csv_file: 
    csv_rows = csv.DictReader(csv_file)

    exams = []
    exams_names = []

    for row in csv_rows: 
        exam_name = row.get("Exam Name") 

        if exam_name not in exams_names: 
            exams.append(Exam(exam_name))
            exams_names.append(exam_name)

        grade = row.get("Grade")
        score = row.get("Score")
        candidate = row.get("Candidate ID")
        
        for exam in exams: 
            if exam_name != exam.name: 
                continue 

            exam.grade.append(grade)
            exam.scores.append(score)
            exam.candidates.append(candidate)

    exams_to_insert = []

    for exam in exams: 
        exam_dict = { 
            "Exam Name": exam.name, 
            "Number of Candidates": exam.return_candidates(),
            "Number of Passed Exams": exam.return_passed(),
            "Number of Failed Exams": exam.return_failed(),
            "Best Score": exam.return_best_score(),
            "Worst Score": exam.return_worst_score()
        }   
        exams_to_insert.append(exam_dict)
        
    create_new_csv(exams_to_insert)
