# hackerrank 1

if __name__ == '__main__':
    grade = []
    student = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student.append([name,score])
        grade.append(score)
        
    grade.sort()
    second_min=0
    mini=grade[0]
    student.sort()
    for i in grade :
        if i != mini:
            second_min=i
            break
    for i in student:
        if i [1]==second_min:
            print(i[0])
            
            
# hackerrank 2

if __name__ == '__main__':
    N = int(input())
    my_lists=[]
    for _ in range(N):
        command = input().split()
        action=command[0]
        
        if action == "insert":
            index=int (command[1])
            value=int(command[2])
            my_lists.insert(index, value)
        elif action == "print" :
            print(my_lists)
        elif action=="remove":
            value=int (command[1])
            my_lists.remove(value)
        elif action=="append":
            value=int(command[1])
            my_lists.append(value)
        elif action=="sort":
            my_lists.sort()
        elif action=="pop":
            my_lists.pop(3)
        elif action == "reverse":
            my_lists.reverse()
        elif action=="print":
            print(my_lists)