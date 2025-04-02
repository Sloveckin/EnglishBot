class InputModel:
    def __init__(self, data):
        self.data = data

    def check_answer(self, exercise, answer):
        return self.data[exercise].upper() == answer.upper()


    def text(self, exercise):
        return exercise

    def get_correct_answer(self, exercise):
        return self.data[exercise]


class TestModel:

    def __init__(self, data):
        self.data = data

    def check_answer(self, exercise, answer):

        if not answer.isnumeric():
            return False

        index = int(answer) - 1

        return index == self.data[exercise][0]


    def text(self, exercise):
        variants = self.data[exercise][1]

        msg = [exercise, '']

        for i in range(len(variants)):
            variant = variants[i]
            msg.append(f"{i + 1}. {variant}")

        return '\n'.join(msg)

    def get_correct_answer(self, exercise):
        correct_index = self.data[exercise][0]
        correct_variant = self.data[exercise][1][correct_index]

        return f"{correct_index + 1}. {correct_variant}"
