movie={
    'name' : 'end game',
    'discription' : 'part 2 of infinity',
    'cost' : 'more than 3 million dollars',
}
print(movie)
a= 'name' in movie
b='nationality' in movie
if a==True:
    print("key 'name' exist in my dictionary")
if a==False:
    print("key 'name' does not exist in my dictionary")
if b==True:
    print("key 'nationality' exist in my dictionary")
if b==False:
    print("key 'nationality' does not exist in my dictionary")