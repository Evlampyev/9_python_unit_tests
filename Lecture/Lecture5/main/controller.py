from calculate import Calculate


class Controller:
    def __init__(self, task):
        self.answer = None
        self.task = task
        self.parsing()
        self.calculating()

    def parsing(self):
        operators = ('*', '/', '+', '-')
        task_list = []
        i = 0
        while len(self.task) > 0 and i < len(self.task):
            if self.task[i] in operators:
                task_list.append(int(self.task[:i]))
                task_list.append(self.task[i])
                self.task = self.task[i + 1:]
                i = 0
            elif not self.task[i].isdigit():
                raise IOError("Неверный ввод")
            else:
                i += 1
        task_list.append(int(self.task))
        self.answer = task_list

    def calculating(self):
        operators = ['*', '/', '+', '-']
        self.task = self.answer
        for operator in operators:
            if self.answer.count(operator) > 0:
                while self.answer.count(operator) > 0:
                    k = self.answer.index(operator)
                    temp_a = self.answer[k - 1]
                    temp_b = self.answer[k + 1]
                    temp_res = Calculate(temp_a, temp_b, operator)
                    self.answer[k - 1] = temp_res.answer
                    del self.answer[k:k + 2]
