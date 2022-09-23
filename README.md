# jcal

`jcal` is a package for Japanese holiday at 2019-2021.
https://www8.cao.go.jp/chosei/shukujitsu/gaiyou.html

## Installation

```
pip install jcal
```

## Example

```python
from pprint import pprint
from jcal import holiday

pprint(holiday(2023))
```

```
{datetime.date(2023, 1, 2),
 datetime.date(2023, 1, 9),
 datetime.date(2023, 2, 11),
 datetime.date(2023, 2, 23),
 datetime.date(2023, 3, 21),
 datetime.date(2023, 4, 29),
 datetime.date(2023, 5, 3),
 datetime.date(2023, 5, 4),
 datetime.date(2023, 5, 5),
 datetime.date(2023, 7, 17),
 datetime.date(2023, 8, 11),
 datetime.date(2023, 9, 18),
 datetime.date(2023, 9, 23),
 datetime.date(2023, 10, 9),
 datetime.date(2023, 11, 3),
 datetime.date(2023, 11, 23)}
```
