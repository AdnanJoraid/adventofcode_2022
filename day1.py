input_data = open("day1.txt", "r")

#part 1 
def solve(input):
    person = 1 
    calories_and_person = [0, 1]
    max_calories = 0  
    result = 0 
    for data in input:
        if data == "\n":
            if calories_and_person[0] > max_calories:
                max_calories = calories_and_person[0] 
                result = calories_and_person[0]
            person += 1 
            calories_and_person = [0, person]
        else:
            calories_and_person[0] += int(data)

    return result 

print(solve(input_data))
input_data.close()
input_data = open("day1.txt", "r")


#part 2 
def solve2(input):
    calories = []
    count = 0 
    for data in input:
        if data == "\n":
            calories.append(count) 
            count = 0 
        else:
            count += int(data) 

    srtd = sorted(calories) 
    return srtd[-1] + srtd[-2] + srtd[-3]

print(solve2(input_data))