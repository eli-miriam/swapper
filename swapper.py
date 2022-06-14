def swapper(n):
    num_as_list = [int(char) for char in str(n)]
    length = len(num_as_list)
    length_of_postfix = None


    # find the first time (working backwards from digits to tens to hundreds, etc)
    # that we find a number that could be bigger. call this number the postfix.
    for i in range(2, length+1):
        current_num = num_as_list[length - i]
        last_num = num_as_list[length - i + 1]
        if current_num < last_num:
            length_of_postfix = i
            break
    
    # we might not find such a scenario; this means the number is already maxed. return False.
    if length_of_postfix is None:
        return False
    
    # We don't care about the prefix, because we want the _next_ biggest number. just store it off.
    prefix = str(n)[0:length - length_of_postfix]

    # now extract (as a string) the postfix that needs to be munged.
    unsorted_postfix = str(n)[length - length_of_postfix:]

    # sort its digits, and find the digit that's next bigger than what was previously its first number.
    sorted_list = sorted([int(char) for char in unsorted_postfix])
    for i, num in enumerate(sorted_list):
        if num > int(unsorted_postfix[0]):
            # remove that next biggest digit from the list
            next_num = sorted_list.pop(i)
    
    # join that next biggest number to the prefix, ensuring that our new number is bigger than the original
    prefix += str(next_num)

    # add the remaining numbers in sorted order to get the smallest possible number out of them
    prefix += "".join([str(i) for i in sorted_list])

    # donezo.
    return int(prefix)


if __name__ == "__main__":
    assert swapper(371) == 713
    assert swapper(3751) == 5137
    assert swapper(731) is False
