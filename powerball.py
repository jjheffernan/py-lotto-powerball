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


# picking the final number
def pick_powerball():
    max_m = 26  # max number = m
    max_j = 1
    m = max_m
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
    lottery_nums = [0] * 6 # could be done more elegantly

    for i in lottery_nums:
        if i == 6:
            lottery_nums[i] = pick_powerball()
        else:
            lottery_nums[i] = pick_lotto()
    print(lottery_nums)
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
            print(pick_lotto())


# immediate-mode commands, for drag-and-drop or execfile() execution
if __name__ == '__main__':
    run()
else:
    print("Module lotto imported.")
    print("To run, type: lotto.run()")
    print("To reload after changes to the source, type: reload(lotto)")

# end of lotto.py
