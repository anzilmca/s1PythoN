class Time:
    def __init__(self, h, m, s):
        self.hour = h
        self.minute = m
        self.second = s

    def __add__(self, T):
        h = self.hour + T.hour
        m = self.minute + T.minute
        s = self.second + T.second

        if s >= 60:
            m = m + s // 60
            s = s % 60

        if m >= 60:
            h = h + m // 60
            m = m % 60

        return Time(h, m, s)

    def display(self):
        print(self.hour, ":", self.minute, ":", self.second)


t1 = Time(2, 40, 50)
t2 = Time(1, 30, 30)

t3 = t1 + t2

print("First time:")
t1.display()

print("Second time:")
t2.display()

print("Sum of time:")
t3.display()
