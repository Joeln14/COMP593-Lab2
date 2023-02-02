def main():

    StudentInfo = {

        'fullname' : 'Joel Niezen',
        'student_id' : '10294961',
        'pizza_toppings' : [
            'BACON',
            'MUSHROOMS',
            'GREEN OLIVES'
        ],
        'movies' : [
            {
                'title' : 'American Psycho',
                'genre' : 'comedy'
            },    
            {
                'title' : 'Dark Knight Rises',
                'genre' : 'thriller'
            }            
        ]  
    } 

    StudentInfo['movies'].append({
        'title' : 'Batman Begins',
        'genre' : 'action'
    })



    print_student_info(StudentInfo)

    print()

    print_pizza_toppings(StudentInfo)

    print()

    add_pizza_toppings(StudentInfo, ('beef', 'sausage'))

    print_pizza_toppings(StudentInfo)

    print()

    print_movie_genres(StudentInfo)

    print()
    
    print_movie_titles(StudentInfo['movies']) 

    




def print_student_info(StudentInfo):

    full_name = StudentInfo['fullname']
    first_name = StudentInfo['fullname']
    student_id = StudentInfo['student_id']

    print(f'My name is {full_name}, but you can call me Sir {first_name.split()[0]}')
    print(f'My student ID is {student_id}')


def add_pizza_toppings(StudentInfo, new_toppings):

    StudentInfo['pizza_toppings'].extend(new_toppings)
    
    for i,t in enumerate(StudentInfo['pizza_toppings']):
        StudentInfo['pizza_toppings'][i] = t.lower()
    
    StudentInfo['pizza_toppings'].sort()


def print_pizza_toppings(StudentInfo):

    print(f"My favourite pizza toppings are:")
    
    for t in StudentInfo['pizza_toppings']:
        print(f'-{t}')


def print_movie_genres(StudentInfo):
    
    print('I like to watch ', end=' ')

    for i,movie in enumerate(StudentInfo['movies']):
      
        if i < len(StudentInfo['movies']) -2:
            print(movie['genre'], end=', ')

        elif i == len(StudentInfo['movies']) -1:
            print(movie['genre'], end=' ')
        
        else:
            print(movie['genre'], end=', and ')
  
    print('movies.')


def print_movie_titles(movies):


    print('Some of my favourite movies are', end=' ')

    for i,movie in enumerate(movies):
    
        if i < len(movies) -2:
            print(movie['title'], end=', ')

        elif i == len(movies) -1:
            print(movie['title'], end='')
        
        else:
            print(movie['title'], end=', and ') 

    print('!') 





if __name__ == '__main__':
    main()