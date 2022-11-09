from mrjob.job import MRJob


class punto1(MRJob):

    def mapper(self, _, line):
        idemp,sector,salary,year = line.split(',')
        yield sector, int(salary)

    def reducer(self, sector, values):
        l = list(values)
        avg = sum(l) / len(l)
        yield sector, avg


if __name__ == '__main__':
    punto1.run()