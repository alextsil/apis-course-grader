# Single grading check result
# True/False = Pass/Fail, assignment = which exercise, notes = reason for pass/fail


class Result:

    def __init__(self, result, assignment, notes):
        self.result = result
        self.assignment = assignment
        self.notes = notes

    def __str__(self) -> str:
        return self.assignment + ", " + (
            "\033[92mPass\033[0m" if self.result else "\033[91mFail\033[0m") + ", " + self.notes
