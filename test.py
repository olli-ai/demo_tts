from typing import Dict, List, Any


# Visitor Interface
class ParserVisitor:
    def visit_rest_api_input(self, input_data) -> Dict[str, Any]:
        pass

    def visit_excel_input(self, input_data) -> Dict[str, Any]:
        pass

    def visit_word_input(self, input_data) -> Dict[str, Any]:
        pass


# Input Data Classes
class InputData:
    def accept(self, visitor: ParserVisitor) -> Dict[str, Any]:
        pass


class RestApiInput(InputData):
    def __init__(self, data: Dict):
        self.data = data

    def accept(self, visitor: ParserVisitor) -> Dict[str, Any]:
        return visitor.visit_rest_api_input(self)


class ExcelInput(InputData):
    def __init__(self, data: List[Dict]):
        self.data = data

    def accept(self, visitor: ParserVisitor) -> Dict[str, Any]:
        return visitor.visit_excel_input(self)


class WordInput(InputData):
    def __init__(self, data: str):
        self.data = data

    def accept(self, visitor: ParserVisitor) -> Dict[str, Any]:
        return visitor.visit_word_input(self)


# Specific Visitors (Parsers)
class DataParser(ParserVisitor):
    def visit_rest_api_input(self, input_data: RestApiInput) -> Dict[str, Any]:
        return {"parsed_data": f"Parsed REST API data: {input_data.data}"}

    def visit_excel_input(self, input_data: ExcelInput) -> Dict[str, Any]:
        return {"parsed_data": f"Parsed Excel data: {input_data.data}"}

    def visit_word_input(self, input_data: WordInput) -> Dict[str, Any]:
        return {"parsed_data": f"Parsed Word data: {input_data.data}"}


# Data Processing
def process_data(input_data: InputData, parser: ParserVisitor) -> None:
    parsed_data = input_data.accept(parser)
    print(f"Processed: {parsed_data}")


# Main function
def main():
    rest_api_data = RestApiInput({"key": "value"})
    excel_data = ExcelInput([{"column1": "row1data"}, {"column1": "row2data"}])
    word_data = WordInput("Text content from a Word document")

    parser = DataParser()

    process_data(rest_api_data, parser)
    process_data(excel_data, parser)
    process_data(word_data, parser)


if __name__ == "__main__":
    main()
