from mrjob.job import MRJob
from mrjob.job import MRStep


class punto4(MRJob):

    def mapper(self, _, line):
        user,movie,rating,genre,date = line.split(',')
        yield movie, int(rating)

    def reducer(self, movie, values):
        l = list(values)
        users = len(l)
        avg = sum(l) / users
        yield ["Movie:", movie], (["Users:", users], ["Avg rating:", avg])


if __name__ == '__main__':
    punto4.run()