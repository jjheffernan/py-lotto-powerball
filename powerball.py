# powerball.py based on lotto picker by manny juan  (juanm@wellsfargo.com or manny@bdt.com)
# re-work done by jj heffernan for Zip Code Wilmington

# imports
from random import randint


# picking a single lottery number
def pick_lotto():

    max_m = 69  # max number = m
    max_j = 5
    m = max_m
    # create all numbers from 0 to m
    r = list(range(m+1))
    # start with an empty result
    v = []
    for j in range(max_j):
        # get ith number from r...
        i = randint(1, m)
        n = r[i]
        # remove it from r...
        r[i:i+1] = []
        m = m - 1
        # and append to the result
        v.append(n)
        return v
    return v


# picking the final number
def pick_powerball():
    pow_m = 26  # max number = m
    max_j = 1
    m = pow_m
    # create all numbers from 0 to m
    r = list(range(m + 1))
    # start with an empty result
    v = []
    for j in range(max_j):
        # get ith number from r...
        i = randint(1, m)
        n = r[i]
        # remove it from r...
        r[i:i + 1] = []
        m = m - 1
        # and append to the result
        v.append(n)
        return v
    # pass  # escape pass


# generating the tuple f
def handle_numbers():
    lottery_nums = ()  # could be done more elegantly

    for i in range(5):
        lotto_val = pick_lotto()
        lottery_nums = lottery_nums + tuple(lotto_val)
        # print(pick_lotto())
        # lottery_nums.append()
    power_val = pick_powerball()
    lottery_nums = lottery_nums + tuple(power_val)
    print(lottery_nums)
    # lottery_nums.append(powerball)
    # print(lottery_nums)

    # pass  # escape pass


def run():
    done = 0

    while not done:
        try:
            x = input('\npress Enter for Lotto picks (Q to quit). ')
        except EOFError:
            x = 'q'
        if x and (x[0] == 'q' or x[0] == 'Q'):
            done = 1
            print('done')
        else:
            # print(pick_lotto())
            handle_numbers()


# immediate-mode commands, for drag-and-drop or execfile() execution
if __name__ == '__main__':
    run()
else:
    print("Module lotto imported.")
    print("To run, type: lotto.run()")
    print("To reload after changes to the source, type: reload(lotto)")

# end of lotto.py
