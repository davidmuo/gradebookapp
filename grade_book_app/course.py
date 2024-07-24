class Course:
    def __init__(self, name, trimester, credits):
        self.name = name
        self.trimester = trimester
        self.credits = credits

    def to_dict(self):
        return {
            'name': self.name,
            'trimester': self.trimester,
            'credits': self.credits
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data['name'], data['trimester'], data['credits'])
