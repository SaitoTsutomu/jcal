import pytest
from holidays import Japan

from jcal import MAX_YEAR, MIN_YEAR, holidays


@pytest.mark.parametrize("year", range(MIN_YEAR, MAX_YEAR + 1))
def test(year):
    h0 = dict(Japan(years=year))
    h1 = {d: d.name for d in holidays(year)}
    df = set(h0) ^ set(h1)
    assert df == set(), f"差分 {df}"
    for dt in h1:
        s0 = h0[dt]
        s1 = h1[dt]
        assert s0 == s1, f"名称違い {dt} {s0} {s1}"
