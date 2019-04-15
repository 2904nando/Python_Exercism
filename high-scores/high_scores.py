class HighScores(object):
    def __init__(self, scores):
        self.scores = scores

    def personal_best(self):
        max_temp = self.scores[0]
        for i in self.scores:
            if i > max_temp:
                max_temp = i
        return max_temp

    def latest(self):
        return self.scores[-1]

    def personal_top_three(self):
        list_temp = self.scores
        list_temp.sort(reverse=True)
        list_best = []
        for i, val in enumerate(list_temp):
            if i < 3:
                list_best.append(val)
        return list_best
