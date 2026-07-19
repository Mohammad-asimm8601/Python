# Write a function that capitalizes the first and fourth letters of a name old_macdonald("macdonald") --> MacDonald

# Method -1 Using Slicing


def old_macdonald(name):
    first_letter = name[:1]
    middle_letter = name[1:3]
    fourth_letter = name[3:4]
    last_letter = name[4:]
    return first_letter.upper() + middle_letter + fourth_letter.upper() + last_letter


result = old_macdonald("macdonald")
print(result)

# Method-2 Using for loop


def old_macdonald(name):
    word = ""
    for index, letter in enumerate(name):
        if index == 0 or index == 3:
            word += letter.upper()

        else:
            word += letter
    return word


result = old_macdonald("macdonald")
print(result)


# * Given a sentence, return a sentence with the words reversed


def reverse_word(text):
    world_list = text.split()
    return " ".join(world_list[::-1])


result = reverse_word("I am Mohammad Asim")
print(result)


# * Given an integer n, return True if n is within 10 either 100 or 200


def almost_there(n):
    if abs(100 - n) <= 10 or abs(200 - n) <= 10:
        return True
    else:
        return False


result = almost_there(104)
print(result)


# *Given a list of ints, return True if the array contains a 3 next to a n somewhere


def has_33(nums):
    for idx in range(0, len(nums) - 1):
        if nums[idx : idx + 2] == [3, 3]:
            return True

    return False


result = has_33([3, 1, 3, 3])
print(result)


# * Given a string, return where for every character in the original there are three characters

def paper_doll(text):
    str = ""
    for letter in text:
        str += letter*3
    return str

result = paper_doll('Hello')
print(result)