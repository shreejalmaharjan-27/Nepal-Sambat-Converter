from NepalSambatConverter import NepalSambatConverter
from datetime import datetime
if __name__ == "__main__":
    converter = NepalSambatConverter()

    date = datetime(2024, 12, 31)
    year, month, day = converter.gregorian_to_nepal_sambat(date)
    result = converter.format_nepal_sambat_date(year, month, day)
    print(f"{date.date()} = NS {result}")
    
    # # Test cases
    # test_dates = [
    #     datetime(2024, 4, 1),    # Should be 1144.05.22
    #     datetime(2022, 4, 1),    # Should be 1142.05.30
    #     datetime(2021, 11, 5),   # Should be 1142.01.01
    #     datetime(2024, 11, 2),   # Should be 1145.01.01
    #     datetime(2025, 1, 21)
    # ]
    
    # for date in test_dates:
    #     try:
    #         year, month, day = converter.gregorian_to_nepal_sambat(date)
    #         result = converter.format_nepal_sambat_date(year, month, day)
    #         print(f"{date.date()} = NS {result}")
            
    #         # Verify reverse conversion
    #         greg_date = converter.nepal_sambat_to_gregorian(year, month, day)
    #         print(f"Converted back: {greg_date.date()}\n")
    #     except ValueError as e:
    #         print(f"Error for {date}: {e}\n")