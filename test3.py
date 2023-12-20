from typing import Dict, List, Any, cast


# Base input class
class InputData:
    pass


# Specific input types
class RestApiInput(InputData):
    def __init__(self, data: Dict):
        self.data = data


class ExcelInput(InputData):
    def __init__(self, data: List[Dict]):
        self.data = data


class WordInput(InputData):
    def __init__(self, data: str):
        self.data = data


# Parser strategy interface
class ParserStrategy:
    def parse(self, data: InputData) -> Dict[str, Any]:
        raise NotImplementedError


# Concrete parser strategies
class RestApiParser(ParserStrategy):
    def parse(self, data: InputData) -> Dict[str, Any]:
        if not isinstance(data, RestApiInput):
            raise TypeError("Expected RestApiInput")
        data = cast(RestApiInput, data)
        return {"parsed_data": f"Parsed REST API data: {data.data}"}


class ExcelParser(ParserStrategy):
    def parse(self, data: InputData) -> Dict[str, Any]:
        if not isinstance(data, ExcelInput):
            raise TypeError("Expected ExcelInput")
        data = cast(ExcelInput, data)
        return {"parsed_data": f"Parsed Excel data: {data.data}"}


class WordParser(ParserStrategy):
    def parse(self, data: InputData) -> Dict[str, Any]:
        if not isinstance(data, WordInput):
            raise TypeError("Expected WordInput")
        data = cast(WordInput, data)
        return {"parsed_data": f"Parsed Word data: {data.data}"}


# Data processor
class DataProcessor:
    def __init__(self, parser: ParserStrategy):
        self.parser = parser

    def process_data(self, data: InputData) -> None:
        parsed_data = self.parser.parse(data)
        print(f"Processed: {parsed_data}")


# Main function
def main():
    rest_api_data = RestApiInput({"key": "value"})
    excel_data = ExcelInput([{"column1": "row1data"}, {"column1": "row2data"}])
    word_data = WordInput("Text content from a Word document")

    rest_api_processor = DataProcessor(RestApiParser())
    rest_api_processor.process_data(rest_api_data)

    excel_processor = DataProcessor(ExcelParser())
    excel_processor.process_data(excel_data)

    word_processor = DataProcessor(WordParser())
    word_processor.process_data(word_data)


if __name__ == "__main__":
    main()
