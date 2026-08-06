from datetime import datetime

class DateHandler:
    @staticmethod
    def today_str():
        return datetime.today().strftime("%Y-%m-%d")

    @staticmethod
    def parse_date(date_str):
        return datetime.strptime(date_str, "%Y-%m-%d")
