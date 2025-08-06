# Test Configuration

## Running Tests

To run all tests:
```bash
python -m pytest tests/ -v
```

To run specific test files:
```bash
python -m pytest tests/test_send_email_tool.py -v
python -m pytest tests/test_doc_lookup_tool.py -v
```

To run tests with coverage (if coverage is installed):
```bash
python -m pytest tests/ --cov=tools --cov-report=html -v
```

## Test Structure

- `tests/test_send_email_tool.py` - Tests for the email sending functionality
- `tests/test_doc_lookup_tool.py` - Tests for the document lookup functionality

## Test Coverage

The tests cover:
- Basic functionality
- Edge cases (empty inputs, None values)
- Error conditions
- Special characters and Unicode support
- Case sensitivity
- Input validation
