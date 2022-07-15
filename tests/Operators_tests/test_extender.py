from PyCircTools import Extender


def test_extender():
    ext = Extender()

    assert ext.set_input([True, True]).get_output() == [True, True, False, False]
    assert ext.get_numIn() == 2
    assert ext.get_numOut() == 4

    _ext = Extender(4, 8)

    assert _ext.numInto == 4
    assert _ext.numOut == 8
    assert _ext.set_input([False, False, True, False]).get_output() == [False, False, True, False, False, False, False,
                                                                        False]
    assert _ext.set_input([True, False, True, True], False).get_output() == [True, False, True, True, True, True, True,
                                                                             True]
