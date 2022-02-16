from calcalc.CalCalc import calculate

###########################################
#                  Tests                  #
###########################################


def test_prevent_os_operations_1():
    try:
        calculate("os.system")
    except:
        assert True
    else:
        assert False


def test_prevent_os_operations_2():
    try:
        calculate("rm ")
    except:
        assert True
    else:
        assert False


def test_prevent_os_operations_3():
    try:
        calculate("-rf")
    except:
        assert True
    else:
        assert False


def test_basic_operations():
    assert 30 - calculate("7 * 4") == 2


def test_wolfram_basic_operations():
    assert (
        calculate("what is the mass of the moon in kg") == "7.3459×10^22 kg (kilograms)"
    )


def test_fail_wolfram_operation():
    assert (
        calculate("what is the average lifespan")
        == "I don't know the answer to that unfortunately, ask something else or be more specific and quantifiable."
    )


def test_invalid_arg_int():
    try:
        not_string_variable = 1
        calculate(not_string_variable)
    except:
        assert True
    else:
        assert False


def test_invalid_arg_list():
    try:
        not_string_variable = [1, 2]
        calculate(not_string_variable)
    except:
        assert True
    else:
        assert False
