import itertools

from PyCircTools import NotTruthValue, NonExistingControlSignal, NonExistingInput
from PyCircTools.Multiplexers import Mux16to1


def generate_inputs(num):
    vals = []
    for i in itertools.product([False, True], repeat=num):
        vals.append(i)

    return vals


def get_expected(val):
    if val[0] == 0 and val[1] == 0 and val[2] == 0 and val[3] == 0:
        return 15
    if val[0] == 0 and val[1] == 0 and val[2] == 0 and val[3] == 1:
        return 14
    if val[0] == 0 and val[1] == 0 and val[2] == 1 and val[3] == 0:
        return 13
    if val[0] == 0 and val[1] == 0 and val[2] == 1 and val[3] == 1:
        return 12
    if val[0] == 0 and val[1] == 1 and val[2] == 0 and val[3] == 0:
        return 11
    if val[0] == 0 and val[1] == 1 and val[2] == 0 and val[3] == 1:
        return 10
    if val[0] == 0 and val[1] == 1 and val[2] == 1 and val[3] == 0:
        return 9
    if val[0] == 0 and val[1] == 1 and val[2] == 1 and val[3] == 1:
        return 8
    if val[0] == 1 and val[1] == 0 and val[2] == 0 and val[3] == 0:
        return 7
    if val[0] == 1 and val[1] == 0 and val[2] == 0 and val[3] == 1:
        return 6
    if val[0] == 1 and val[1] == 0 and val[2] == 1 and val[3] == 0:
        return 5
    if val[0] == 1 and val[1] == 0 and val[2] == 1 and val[3] == 1:
        return 4
    if val[0] == 1 and val[1] == 1 and val[2] == 0 and val[3] == 0:
        return 3
    if val[0] == 1 and val[1] == 1 and val[2] == 0 and val[3] == 1:
        return 2
    if val[0] == 1 and val[1] == 1 and val[2] == 1 and val[3] == 0:
        return 1
    if val[0] == 1 and val[1] == 1 and val[2] == 1 and val[3] == 1:
        return 0


def test_Mux16to1():
    errors = []
    mux = Mux16to1()
    inputs = generate_inputs(16)
    set_inputs = generate_inputs(4)

    for val in inputs:
        mux.set_input(0, val[15]).set_input(1, val[14]).set_input(2, val[13]).set_input(3, val[12])\
            .set_input(4, val[11]).set_input(5, val[10]).set_input(6, val[9]).set_input(7, val[8])\
            .set_input(8, val[7]).set_input(9, val[6]).set_input(10, val[5]).set_input(11, val[4])\
            .set_input(12, val[3]).set_input(13, val[2]).set_input(14, val[1]).set_input(15, val[0])

        for set_val in set_inputs:
            mux.set_set(0, set_val[3]).set_set(1, set_val[2]).set_set(2, set_val[1]).set_set(3, set_val[0])
            expected = val[get_expected(set_val)]
            output = mux.get_output()

            if output != expected:
                to_append = "{}".format(str(val[15])) + ", {}".format(str(val[14])) + \
                            ", {}".format(str(val[13])) + ", {}".format(str(val[12])) + ", {}".format(str(val[11])) + \
                            ", {}".format(str(val[10])) + ", {}".format(str(val[9])) + ", {}".format(str(val[8])) + \
                            ", {}".format(str(val[7])) + ", {}".format(str(val[6])) + ", {}".format(str(val[5])) + \
                            ", {}".format(str(val[4])) + ", {}".format(str(val[3])) + ", {}".format(str(val[2])) + \
                            ", {}".format(str(val[1])) + ", {}".format(str(val[0])) +\
                            ", set signals {}".format(str(set_val[3])) + ", {}".format(str(set_val[2])) + \
                            ", {}".format(str(set_val[1])) + ", {}".format(str(set_val[0])) + \
                            " test not passed!"
                errors.append(to_append)

    try:
        mux.set_set(5, False)
        errors.append("Not existing set input test not passed!")
    except NonExistingControlSignal:
        pass

    try:
        mux.set_set(0, 5)
        errors.append("Not truth value to set test not passed!")
    except NotTruthValue:
        pass

    try:
        mux.set_input(16, False)
        errors.append("Not existing input test not passed!")
    except NonExistingInput:
        pass

    assert not errors, "errors occurred:\n{}".format("\n".join(errors))
