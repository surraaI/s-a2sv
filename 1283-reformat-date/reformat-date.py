class Solution:
    def reformatDate(self, date: str) -> str:
        
        month_map = {
            "Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04",
            "May": "05", "Jun": "06", "Jul": "07", "Aug": "08",
            "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"
        }
        day_str, month_str, year_str = date.split()
        day = day_str[:-2]
        if len(day) == 1:
            day = "0" + day
        month = month_map[month_str]

       
        formatted_date = f"{year_str}-{month}-{day}"

        return formatted_date
