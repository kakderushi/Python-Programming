class Movie(object):
    def __init__(self, title, runtime, hero):
        self.title = title
        self.runtime = runtime
        self.hero = hero
        
    def printer(self):
        print(f"title is: {self.title}\nruntime is: {self.runtime} mins\nhero is: {self.hero}")
        
        
listOfMovies = []  
while True:
    title = input("Enter the title of the movie: ")
    runtime = input("Enter the runtime of the movie in minutes: ")
    hero = input("Enter the name of the hero in the movie: ")
    obj = Movie(title, runtime, hero)
    listOfMovies.append(obj)
    print("Movie added to the list.")
    
    ans = input("Do you want to add another movie (y/n)? ")
    if ans.lower() != 'y':
        break
    
print("\nAll Movie Information:")
for obj in listOfMovies:
    obj.printer()
