from datetime import datetime, timedelta
from typing import Tuple, Dict, List

class NepalSambatConverter:
    def __init__(self):
        self.MONTH_NAMES = [
            "Kachhalā", "Thinlā", "Pwanhelā", "Silā", "Chilā", "Chaulā",
            "Bachhalā", "Tachhalā", "Dilā", "Gunlā", "Yanlā", "Kaulā", "Analā"
        ]

        # Define new year dates for some years to establish pattern
        self.NEW_YEAR_DATES = {
            1141: datetime(2020, 11, 16),
            1142: datetime(2021, 11, 5),
            1143: datetime(2022, 10, 26),
            1144: datetime(2023, 11, 14),
            1145: datetime(2024, 11, 2)
        }

        # Define month patterns for various years
        self.MONTH_PATTERNS = {
            1144: [29, 30, 29, 30, 29, 30, 29, 30, 29, 30, 29, 30],
            1145: [30, 29, 30, 30, 29, 28, 31, 29, 29, 30, 29, 30]
        }

    def _get_month_lengths(self, year: int) -> List[int]:
        """Get the month lengths for a specific year."""
        if year in self.MONTH_PATTERNS:
            return self.MONTH_PATTERNS[year]
        
        # For years without specific patterns, use the alternating 29/30 pattern
        # This is a basic approximation and should be enhanced
        return [30 if i % 2 == 0 else 29 for i in range(12)]

    def _find_year_bounds(self, date: datetime) -> Tuple[int, datetime, datetime]:
        """Find the Nepal Sambat year that contains the given date."""
        for year in sorted(self.NEW_YEAR_DATES.keys()):
            year_start = self.NEW_YEAR_DATES[year]
            next_year = year + 1
            year_end = (self.NEW_YEAR_DATES[next_year] 
                       if next_year in self.NEW_YEAR_DATES 
                       else year_start + timedelta(days=365))
            
            if year_start <= date < year_end:
                return year, year_start, year_end
        
        raise ValueError(f"Date {date} is outside the supported range")

    def gregorian_to_nepal_sambat(self, date: datetime) -> Tuple[int, int, int]:
        """Convert a Gregorian date to Nepal Sambat date."""
        year, year_start, _ = self._find_year_bounds(date)
        days_since_new_year = (date - year_start).days
        
        # Get month lengths for this year
        month_lengths = self._get_month_lengths(year)
        
        # Find month and day
        days_counted = 0
        for month_num, month_length in enumerate(month_lengths, 1):
            if days_since_new_year < days_counted + month_length:
                day = days_since_new_year - days_counted + 1
                return year, month_num, day
            days_counted += month_length
        
        raise ValueError("Date calculation error")

    def nepal_sambat_to_gregorian(self, year: int, month: int, day: int) -> datetime:
        """Convert a Nepal Sambat date to Gregorian date."""
        if year not in self.NEW_YEAR_DATES:
            raise ValueError(f"Year {year} is outside the supported range")
        
        # Get year start date and month lengths
        year_start = self.NEW_YEAR_DATES[year]
        month_lengths = self._get_month_lengths(year)
        
        if not 1 <= month <= len(month_lengths):
            raise ValueError(f"Invalid month {month} for year {year}")
        
        if not 1 <= day <= month_lengths[month - 1]:
            raise ValueError(f"Invalid day {day} for month {month}")
        
        # Calculate days to add to year start
        days_to_add = sum(month_lengths[:month - 1]) + (day - 1)
        
        return year_start + timedelta(days=days_to_add)

    def format_nepal_sambat_date(self, year: int, month: int, day: int) -> str:
        """Format a Nepal Sambat date as a string."""
        return f"{year}.{month:02d}.{day:02d} ({self.MONTH_NAMES[month-1]})"