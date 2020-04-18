from jcal import holiday


def test_holiday():
    actual = " ".join(f"{dt.month}/{dt.day}" for dt in sorted(holiday(2019)))
    expect = (
        "1/1 1/14 2/11 2/23 3/21 4/29 4/30 5/1 5/2 5/3 5/4 5/5 5/6 "
        "7/15 8/12 9/16 9/23 10/14 10/22 11/4 11/23"
    )
    assert actual == expect
