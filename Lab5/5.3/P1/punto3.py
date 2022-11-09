from mrjob.job import MRJob


class punto3(MRJob):

    def mapper(self, _, line):
        idemp, sector,salary,year = line.split(',')
        yield idemp, sector

    def reducer(self, idemp, values):
        l = len(set(values))
        yield idemp, l


if __name__ == '__main__':
    punto3.run()