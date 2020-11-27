""" Recursion is the repeated application of the same procedure to a smaller problem.
Imagine you're in a line of people and you want to know how many people are in front of
you. If the line is long, it might be hard to count the people without leaving the line
and losing your place. Instead you can ask the person in front of you how many people are
in front of them. Since this person will be in the same situation as you, they'll have to
ask the same question to the person in front of them and so on and so on until the question
reaches the first person in the line. This person can confidently reply that there are no
people in front of them. So then the second person in line can reply one, the person behind
them replies two, and so on until the answer reaches you.

In programming, recursion is a way of doing a repetitive task by having a function call
itself. A recursive function calls itself usually with a modified parameter until it reaches
a specific condition. This condition is called the base case.

A recursive function will usually have this structure:

def recursive_function(parameters):
    if base_case_condition(parameters):
        return base_case_value
    recursive_function(modified_parameters)

"""

def sum_positive_numbers(n):
    # The base case is n being smaller than 1
    if n < 1:
        return n

    # The recursive case is adding this number to
    # the sum of the numbers smaller than this one.
    return n + sum_positive_numbers(n-1)

print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15
print()



def is_power_of(number, base):
  number = number/base
  # Base case: when number is smaller than base.
  if number < base:
    # If number is equal to 1, it's a power (base**0).
    return False
  else:
    return True

  # Recursive case: keep dividing number by base.
  return is_power_of(number, base)

print(is_power_of(8,2)) # Should be True
print(is_power_of(64,4)) # Should be True
print(is_power_of(70,10)) # Should be False
print()


