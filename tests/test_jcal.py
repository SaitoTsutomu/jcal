from jcal import holiday


def test_holiday2019():
    actual = " ".join(f"{dt.month}/{dt.day}" for dt in sorted(holiday(2019)))
    expect = (
        "1/1 1/14 2/11 3/21 4/29 4/30 5/1 5/2 5/3 5/4 5/5 5/6 "
        "7/15 8/12 9/16 9/23 10/14 10/22 11/4 11/23"
    )
    assert actual == expect


def test_holiday2020():
    actual = " ".join(f"{dt.month}/{dt.day}" for dt in sorted(holiday(2020)))
    expect = (
        "1/1 1/13 2/11 2/24 3/20 4/29 5/4 5/5 5/6 7/23 7/24 8/10 9/21 9/22 11/3 11/23"
    )
    assert actual == expect


def test_holiday2021():
    actual = " ".join(f"{dt.month}/{dt.day}" for dt in sorted(holiday(2021)))
    expect = (
        "1/1 1/11 2/11 2/23 3/20 4/29 5/3 5/4 5/5 7/22 7/23 8/9 9/20 9/23 11/3 11/23"
    )
    assert actual == expect


def test_holiday2022():
    actual = " ".join(f"{dt.month}/{dt.day}" for dt in sorted(holiday(2022)))
    expect = (
        "1/1 1/10 2/11 2/23 3/21 4/29 5/3 5/4 5/5 7/18 8/11 9/19 9/23 10/10 11/3 11/23"
    )
    assert actual == expect
