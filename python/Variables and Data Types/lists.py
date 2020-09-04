# you can think lists as an array
# Mutable

dist_name = ['Dhaka','Rajshahi','Sylhet','Barishal','Khulna'] 
print(type(dist_name))
print(dist_name[0])
print(dist_name[-1])
print(dist_name[1:4])


car_number_plate = ['E-1828','A-1212','F-2261','E-1121']
print(car_number_plate)
car_number_plate.append('B-1272')
print(car_number_plate)
car_number_plate.pop()
print(car_number_plate)
car_number_plate.insert(3,'C-1512')
print(car_number_plate)
del car_number_plate[2:4]
print(car_number_plate)
car_number_plate.clear()
print(car_number_plate)

numbers = [1,1,2,3,5,8,13,21,34]
print(numbers)
print(max(numbers))
print(min(numbers))
print(sum(numbers))