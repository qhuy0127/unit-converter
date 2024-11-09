# Unit Converter

A simple yet powerful command-line tool for converting between different units of measurement. This tool supports conversions for temperature (Celsius/Fahrenheit), distance (Kilometers/Miles), and weight (Kilograms/Pounds).

## Features

- Convert between multiple unit types:
  - Temperature: Celsius ↔ Fahrenheit
  - Distance: Kilometers ↔ Miles
  - Weight: Kilograms ↔ Pounds
- Command-line interface with clear usage instructions
- Error handling and input validation
- Clear and formatted output

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/qhuy0127/unit-converter.git
   ```
2. Navigate to the project directory:
   ```bash
   cd unit-converter
   ```
3. Make the script executable (Unix-based systems):
   ```bash
   chmod +x unit_converter.py
   ```

## Usage

The basic syntax is:
```bash
python unit_converter.py VALUE CONVERSION_TYPE
```

Available conversion types:
- `c2f`: Celsius to Fahrenheit
- `f2c`: Fahrenheit to Celsius
- `km2mi`: Kilometers to Miles
- `mi2km`: Miles to Kilometers
- `kg2lb`: Kilograms to Pounds
- `lb2kg`: Pounds to Kilograms

### Examples

1. Convert 25 degrees Celsius to Fahrenheit:
   ```bash
   python unit_converter.py 25 c2f
   ```

2. Convert 10 kilometers to miles:
   ```bash
   python unit_converter.py 10 km2mi
   ```

3. Convert 150 pounds to kilograms:
   ```bash
   python unit_converter.py 150 lb2kg
   ```

## Error Handling

The tool includes error handling for:
- Invalid input values
- Incorrect conversion types
- General runtime errors

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.