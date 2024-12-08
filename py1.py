import requests
class Fetcher:
    def __init__(self):
        url = "https://cdn.ituring.ir/ex/users.json"
        response = requests.get(url)
        response.raise_for_status()  
        self._students = response.json()
    def nerds(self):
        """
        returns a set of full names (first name + last name) of students with score > 18.5
        """
        return {
            f"{student['firstName']} {student['lastName']}"
            for student in self._students
            if student.get('score', 0) > 18.5
        }
    def sultans(self):
        """
        returns a tuple of full names of students with the highest score
        """
        if not self._students:
            return ()
        max_score = max(student.get('score', 0) for student in self._students)
        return tuple(
            f"{student['firstName']} {student['lastName']}"
            for student in self._students
            if student.get('score', 0) == max_score
        )
    def mean(self):
        """
        returns the mean score of all students
        """
        scores = [student.get('score', 0) for student in self._students]
        return sum(scores) / len(scores) if scores else 0
    def get_students(self):
        """
        returns a list of dictionaries containing students' data without city, province, and location
        """
        return [
            {
                key: value
                for key, value in student.items()
                if key not in {'city', 'province', 'location'}
            }
            for student in self._students
        ]