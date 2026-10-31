import calendar as _calendar
import datetime as dt

from .holidays import holidays

_WEEKDAYS = "月火水木金土日"


class ColorHTMLCalendar(_calendar.HTMLCalendar):
    """色付きHTMLカレンダー"""

    def formatweekday(self, day: int) -> str:
        cls = self.cssclasses_weekday_head[day]
        if day == _calendar.SUNDAY:
            cls += " holiday"
        elif day == _calendar.SATURDAY:
            cls += " saturday"
        return f'<th class="{cls}">{_WEEKDAYS[day]}</th>'

    def formatmonthname(self, theyear: int, themonth: int, withyear: bool = True) -> str:  # ruff:ignore[boolean-type-hint-positional-argument, boolean-default-value-positional-argument]
        s = f"{theyear}年{themonth}月" if withyear else f"{themonth}月"
        return f'<tr><th colspan="7" class="{self.cssclass_month_head}">{s}</th></tr>'

    def formatmonth(self, theyear: int, themonth: int, withyear: bool = True) -> str:  # ruff:ignore[boolean-type-hint-positional-argument, boolean-default-value-positional-argument]
        self.current_year = theyear
        self.current_month = themonth
        self.holiday_set = holidays(theyear)
        return super().formatmonth(theyear, themonth, withyear)

    def formatday(self, day: int, weekday: int) -> str:
        if day == 0:
            return '<td class="noday">&nbsp;</td>'
        date = dt.date(self.current_year, self.current_month, day)
        if weekday == _calendar.SUNDAY or date in self.holiday_set:
            cls = "holiday"  # 日曜日または祝日
        elif weekday == _calendar.SATURDAY:
            cls = "saturday"  # 土曜日
        else:
            cls = "weekday"  # 平日
        return f'<td class="{cls}">{day}</td>'


_STYLE = """
<style>
.calendar-container { font-family: sans-serif; }
table { border-collapse: collapse; margin: 0; }
td, th { padding: 4px; text-align: center; border: 1px solid #ddd; vertical-align: top; }
th { background-color: #f8f8f8; }
.holiday { color: red; font-weight: bold; }
.saturday { color: blue; }
.weekday { color: black; }
.noday { background-color: #eee; }
</style>
"""


def calendar_html(year: int) -> str:
    """色付きHTMLカレンダー"""
    return f"<div class='calendar-container'>{_STYLE}{ColorHTMLCalendar().formatyear(year)}</div>"


def calendar_html2(year1: int, year2: int) -> str:
    """2年分の色付きHTMLカレンダー"""
    cal = ColorHTMLCalendar()
    s1 = cal.formatyear(year1)
    s2 = cal.formatyear(year2)
    return f"<div class='calendar-container'>{_STYLE}<table><tr><td>{s1}</td><td>{s2}</td></tr></table></div>"
