import csv
import pandas as pd


# Create micro library that allows users to work with notes about ukrainian films.
# Note should contain film_name, note, rating (rating - is 1 - 5 rating of the film)
# Micro lib should contain the next funcitonality:
#
#     Read notes from .csv file
#     Add note to .csv file
#     Remove note from .csv file
#     Print notes to console
#     Get films with the highest rating
#     Get films with the lowest rating
#     Get average rating among all films

class UAFilms(object):
    def __init__(self, notes):
        self.notes = notes

    def getHighestRating(self, amount=1):
        return self.notes['rating'].nlargest(amount)

    def getLowestRating(self, amount=1):
        return self.notes['rating'].nsmallest(amount)

    def getAverageRating(self):
        return self.notes["rating"].sum() / len(self.notes)


class NoteReader(object):
    def __init__(self, csvfile):
        self.csvfile = csvfile

    def readAll(self):
        df = pd.read_csv(self.csvfile, sep='\t')
        return df

    def add(self, note):
        with open(self.csvfile, 'a') as file:
            file.write(note)

    def remove(self, index):
        df = pd.read_csv(self.csvfile)
        df = df.drop(index=[index])
        df.to_csv(file, index=False)

    def printAll(self):
        for index, row in self.readAll().iterrows():
            print(row)


if __name__ == "__main__":
    some_csv = r"D:\Firefox downloads\films.csv"
    nr = NoteReader(some_csv)
    nr.printAll()
    uaf = UAFilms(nr.readAll())
    print(uaf.getHighestRating())
    print(uaf.getLowestRating())
    print(uaf.getAverageRating())
