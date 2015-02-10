start_number = int(input("What number would you like me to begin with?"))
end_number = int(input("What number would you like me to end with?"))
count_number = int(input("How much would you like me to count by? " +
                     "(Note: for most accurate results have me count by a number " +
                     "that divides evenly into the number you assigned me to end with.)"))

print("\ncalculating...\n")

if start_number < end_number:
   end_number += count_number
   for number in range (start_number, end_number, count_number):
      print(number)

elif end_number < start_number:
   count_number *= -1
   for number in range (end_number, start_number, count_number):
      pyprint(number)


