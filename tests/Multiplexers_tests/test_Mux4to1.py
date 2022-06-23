from CTools import NotTruthValue, NonExistingControlSignal, NonExistingInput
from CTools.Multiplexers import Mux4to1


def to_bool(value):
    if value == 0:
        return False
    else:
        return True


def get_expected(val):
    if val[0] == 0 and val[1] == 0:
        return 3
    elif val[0] == 0 and val[1] == 1:
        return 2
    elif val[0] == 1 and val[1] == 0:
        return 1
    elif val[0] == 1 and val[1] == 1:
        return 0


def test_Mux4to1():
    errors = []
    mux = Mux4to1()
    inputs = [(0, 0, 0, 0), (0, 0, 0, 1), (0, 0, 1, 0), (0, 0, 1, 1), (0, 1, 0, 0), (0, 1, 0, 1), (0, 1, 1, 0),
              (0, 1, 1, 1), (1, 0, 0, 0), (1, 0, 0, 1), (1, 0, 1, 0), (1, 0, 1, 1), (1, 1, 0, 0), (1, 1, 0, 1),
              (1, 1, 1, 0), (1, 1, 1, 1)]
    set_values = [(0, 0), (0, 1), (1, 0), (1, 1)]
    for val in inputs:
        mux.set_input(0, to_bool(val[3])).set_input(1, to_bool(val[2])).set_input(2, to_bool(val[1]))\
            .set_input(3, to_bool(val[0]))
        for set_val in set_values:
            mux.set_set(0, to_bool(set_val[1])).set_set(1, to_bool(set_val[0]))
            expected = val[get_expected(set_val)]
            output = mux.get_output()
            if output != expected:
                to_append = "{}".format(str(to_bool(val[3]))) + ", {}".format(str(to_bool(val[2]))) + \
                            ", {}".format(str(to_bool(val[1]))) + ", {}".format(str(to_bool(val[0]))) + \
                            ", set signals {}".format(str(to_bool(set_val[1]))) + \
                            ", {}".format(str(to_bool(set_val[0]))) + " test not passed!"

                errors.append(to_append)

    try:
        mux.set_set(2, False)
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

    assert not errors, "errors occured:\n{}".format("\n".join(errors))
