def get_digits(number):
    thousands = number // 1000
    hundreds = (number % 1000) // 100
    tens = (number % 100) // 10
    ones = number % 10

    return [thousands, hundreds, tens, ones]

def are_all_digits_identical(digits):
    return len(set(digits)) == 1

def sort_digits_desc(digits):
    for i in range(len(digits)):
        for j in range(i + 1, len(digits)):
            if digits[i] < digits[j]:
                digits[i], digits[j] = digits[j], digits[i]

def sort_digits_asc(digits):
    for i in range(len(digits)):
        for j in range(i + 1, len(digits)):
            if digits[i] > digits[j]:
                digits[i], digits[j] = digits[j], digits[i]

def form_number(digits):
    return digits[0] * 1000 + digits[1] * 100 + digits[2] * 10 + digits[3]

def kaprekar_routine(number):
    count = 0

    while number != 6174:
        digits = get_digits(number)

        if are_all_digits_identical(digits):
            print(f"All digits are identical. Kaprekar's routine will not converge.")
            break

        sort_digits_desc(digits)
        desc_number = form_number(digits)

        sort_digits_asc(digits)
        asc_number = form_number(digits)

        number = desc_number - asc_number

        count += 1
        print(f"Iteration {count}: {desc_number} - {asc_number} = {number}")

    if number == 6174:
        print("Got the Kaprekar's number 6174")

number = int(input("Enter a four digit number: "))
kaprekar_routine(number)
