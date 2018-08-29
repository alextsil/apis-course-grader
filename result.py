# Single grading check result
# True/False = Pass/Fail, assignment = which exercise, notes = reason for pass/fail


class Result:

    def __init__(self, result, assignment, notes):
        self.result = result
        self.assignment = assignment
        self.notes = notes

    def __str__(self) -> str:
        return self.assignment + ", " + ("Pass" if self.result else "Fail") + ", " + self.notes
