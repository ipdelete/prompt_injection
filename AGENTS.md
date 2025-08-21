# AGENTS.md

## Project Overview

This is a **security research repository** demonstrating prompt injection vulnerabilities in AI/LLM-powered agents. The project shows how malicious content hidden within documents can manipulate AI agents into performing unintended actions, such as data exfiltration.

⚠️ **Security Research Project**: This repository contains intentionally vulnerable code for educational and research purposes.

## Setup Commands

```bash
# Install dependencies using uv (recommended)
uv sync

# Alternative: Install with pip
pip install -e .

# Verify installation
python -c "import tools; print('Setup successful')"
```

## Project Structure

- `main.py` - Simple demo showing basic tool functionality
- `tools/` - Core tool implementations with intentional vulnerabilities
  - `send_email_tool.py` - Mock email sending functionality
  - `doc_lookup_tool.py` - Document retrieval with embedded prompt injection
- `mock_attack/` - Advanced vulnerability demonstrations
  - `vuln_agent.py` - Sophisticated vulnerable AI agent simulation
  - `mock_attack_simple.py` - Simple attack demonstration
  - `test_scenarios.py` - Comprehensive test scenarios
- `tests/` - Unit tests for individual components

## Running the Project

### Basic Demo
```bash
# Run the main demonstration
python main.py
```

### Mock Attack Scenarios
```bash
# Run simple attack demonstration
python mock_attack/mock_attack_simple.py

# Run comprehensive test scenarios
python mock_attack/test_scenarios.py

# Run the vulnerable agent simulation
python mock_attack/vuln_agent.py
```

## Testing

```bash
# Run all tests
pytest

# Run tests with verbose output
pytest -v

# Run specific test file
pytest tests/test_doc_lookup_tool.py

# Run tests with coverage (if coverage is installed)
pytest --cov=tools
```

## Code Style Guidelines

- **Python 3.11+** required
- Follow PEP 8 style guidelines
- Use type hints where appropriate
- Include docstrings for public functions and classes
- Keep security-related code clearly documented
- Use descriptive variable names, especially for security-critical components

## Security Considerations

**⚠️ IMPORTANT**: This repository contains intentionally vulnerable code:

1. **Never deploy this code in production** - it contains deliberate security flaws
2. **Prompt injection vulnerabilities** are intentionally implemented for research
3. **Mock email functionality** - all emails are logged, not actually sent
4. **Data exfiltration scenarios** are simulated for educational purposes

### Key Vulnerabilities Demonstrated

- **Document-based prompt injection** in `tools/doc_lookup_tool.py`
- **Multi-pass agent manipulation** in `mock_attack/vuln_agent.py`
- **Social engineering through hidden instructions** in document content

## Development Guidelines

### Adding New Attack Scenarios

1. Create test cases in `tests/` first
2. Implement scenarios in `mock_attack/`
3. Document the vulnerability type and impact
4. Include logging for security event analysis

### Modifying Tools

1. Maintain backward compatibility with existing demos
2. Update corresponding tests
3. Document any new vulnerability patterns
4. Ensure mock services remain clearly marked as such

### Testing New Vulnerabilities

1. Write comprehensive test cases
2. Include both positive and negative test scenarios
3. Document expected vs. actual behavior
4. Test with different input variations

## Dependencies

- `pytest>=8.4.1` - Testing framework
- `pyyaml>=6.0.2` - Configuration file parsing
- Python 3.11+ - Required runtime

## Common Commands

```bash
# Development setup
uv sync
python -m pytest

# Run full demonstration suite
python main.py
python mock_attack/test_scenarios.py

# Debug specific vulnerability
python -c "from tools.doc_lookup_tool import lookup_document; print(lookup_document('vendor_summary.pdf'))"

# Check code formatting (if black is installed)
black --check .

# Type checking (if mypy is installed)
mypy tools/ mock_attack/
```

## Research Context

This project demonstrates:
- How seemingly innocent document content can contain malicious instructions
- Multi-pass processing vulnerabilities in AI agents
- Data exfiltration through prompt injection
- Social engineering techniques targeting AI systems

Use this code responsibly for security research, education, and developing better AI safety practices.