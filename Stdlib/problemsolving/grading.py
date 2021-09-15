def gradingstudents(grades):
    final_grades=[]
    for i in grades:
        if i < 38:
            final_grades.append(i)
        elif i%5 > 3:
            final_grades.append(i)
        elif i%5 <3 :
            i = (int(i/5)+1)*5
            final_grades.append(i)
    
    print(final_grades)

gradingstudents([73,67,38,33])