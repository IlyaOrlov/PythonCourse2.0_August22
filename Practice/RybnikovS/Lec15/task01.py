def give_me_if_error(func):
    def inside_func(a):
        try:
            output = func(a)
            return output
        except ValueError:
            print("\033[31mERROR: NonValidInput".format())
            exit(666)
        except IndexError:
            print("\033[31mERROR: Input number more than 5000".format())
            exit(555)
    return inside_func


@give_me_if_error
def to_roman(input_data):
    input_data = int(input_data)
    ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    hunds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    thous = ["", "M", "MM", "MMM", "MMMM"]
    t = thous[input_data // 1000]
    h = hunds[input_data // 100 % 10]
    te = tens[input_data // 10 % 10]
    o = ones[input_data % 10]
    return t + h + te + o


a = to_roman("4999")
print(a)
