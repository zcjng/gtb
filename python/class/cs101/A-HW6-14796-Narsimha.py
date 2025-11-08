from datetime import date

month_map = { 'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12 }


dates = input().split(',') 

newDates = []
for i in dates:
    x = i.strip()
    newDates.append(x)
    
def parser(s):
    s = s.strip()
    
    if '-' in s and s[:4].isdigit():
        y, m, d = map(int, s.split('-'))
        return date(y, m, d)
    
    elif '/' in s:
        m, d, y = map(int, s.split('/'))
        return date(y, m, d)
    
    else:
        parts = s.split()
        d = int(parts[0])
        m = month_map[parts[1]]
        y = int(parts[2])
        return date(y, m, d)

sort_dates = []
for i in newDates:
    sorting = parser(i)
    sort_dates.append(sorting)
    
sorted_dates = sorted(newDates, key=parser)

print(sort_dates)