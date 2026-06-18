import calendar as _calendar
import datetime

from . import holidays

_calendar.day_abbr = ["月", "火", "水", "木", "金", "土", "日"]
_calendar.month_name = ["", "1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月", "9月", "10月", "11月", "12月"]


class ColorHTMLCalendar(_calendar.HTMLCalendar):
    """色付きHTMLカレンダー"""

    def formatmonth(self, theyear: int, themonth: int, withyear: bool = True) -> str:  # noqa: FBT001 FBT002
        self.current_year = theyear
        self.current_month = themonth
        self.holiday_set = holidays(theyear)
        return super().formatmonth(theyear, themonth, withyear)

    def formatday(self, day: int, weekday: int) -> str:
        if day == 0:
            return '<td class="noday">&nbsp;</td>'
        dt = datetime.date(self.current_year, self.current_month, day)
        if weekday == _calendar.SUNDAY or dt in self.holiday_set:
            cls = "holiday"  # 日曜日または祝日
        elif weekday == _calendar.SATURDAY:
            cls = "saturday"  # 土曜日
        else:
            cls = "weekday"  # 平日
        return f'<td class="{cls}">{day}</td>'


def calendar_html(year: int) -> str:
    """色付きHTMLカレンダー"""
    cal = ColorHTMLCalendar()
    html_content = cal.formatyear(year)
    style = """
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
    return f"<div class='calendar-container'>{style}{html_content}</div>"


def calendar_html2(year1: int, year2: int) -> str:
    """2年分の色付きHTMLカレンダー"""
    s1 = calendar_html(year1)
    s2 = calendar_html(year2)
    return f"<table><tr><td>{s1}</td><td>{s2}</td></tr></table>"
