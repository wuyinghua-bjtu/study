import datetime


class qmks:
    def __init__(self, **d):
        self.ks = d

    def xzks(self, km, sj):
        self.ks[km] = sj
        count = 0
        for k, v in self.ks.items():
            count += 1
        print(count)

    def ckks(self):
        for k, v in self.ks.items():
            now = datetime.datetime.today()
            dtks = datetime.datetime(int(self.ks[k][:4]), int(self.ks[k][5:7]), int(self.ks[k][8:10]),
                                     int(self.ks[k][11:13]), int(self.ks[k][14:16]))
            if now.date().__gt__(dtks.date()):
                judge = '已过'
                flag = 1
            elif now.date().__eq__(dtks.date())and now.time().__gt__(dtks.time()):
                judge = '已过'
                flag = 1
            else:
                judge = '还剩'
                flag = 0
            if flag == 1:
                print(k + '的考试时间是' + v + '距离现在' + judge + str(now - dtks))
            elif flag == 0:
                print(k + '的考试时间是' + v + '距离现在' + judge + str(dtks - now))

student1 = qmks(sysjfx='2020/10/19 08:30', sjwj='2020/12/30 14:00')
student2 = qmks(sysjfx='2020/10/19 08:30')
student1.xzks('tjx','2020/12/12 14:00')
student1.ckks()
