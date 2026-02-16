from typing import Any


class Movie:
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration
    
    def __str__(self):
        return f"{self.title} ({self.duration} min)"

    def __add__(self, other):
        if isinstance(other, Movie):
            return self.duration + other.duration
        else:
            return NotImplemented

    def __eq__(self, other):
        if not isinstance(other, Movie):
            return NotImplemented
        return self.title == other.title and self.duration == other.duration




class Library:
    def __init__(self, movies):
        self.movies = movies
    
    def __getitem__(self, item):
        return self.movies[item]
    
    def __len__(self):
        return len(self.movies)
    
    def __str__(self):
        result = ""
        i = 1
        for movie in self.movies:
            result += str(i) + ". " + str(movie) + "\n"
            i += 1
        return result.strip()



class User:
    view_count = 0
    def __init__(self, name, library):
        self.name = name
        self.library = library

    def __call__(self, *args, **kwds):
        User.view_count += 1
        return f"{self.name} is watching a movie "
    
    def __str__(self):
        return f"{self.name} | Movies: {self.view_count}"
    


m1 = Movie("Matrix", 136)
m2 = Movie("Inception", 148)
m3 = Movie("Interstellar", 169)
library = Library([m1, m2, m3])
user = User("Alex", library)
print(m1)
print(m1 + m2)
print(m1 == m2)
print(library[1])
print(len(library))
print(library)
print(user)
user()
 