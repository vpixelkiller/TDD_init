# Squba — Minimal Setup

## Requirements
- **Python 3**: Confirm it is installed. 
Run `python3 --version` on macOS/Linux
ó
- **Javascript**: Confirm it is installed. 
Run `node --version` on macOS/Linux

## Python environment setup
1. From the project root, create a virtual environment:
   ```
   python3 -m venv file
   ```

2. Activate the environment for your platform:
   - macOS/Linux: `source file/bin/activate`


3. Install pytest while the env is active:
   ```
   pip3 install pytest
   ```
   (If only `pip` is available, use it instead, remember the class.)

### Ready to go
- Run `pytest` and enjoy a smooth test-driven flow.

## Javascript environment setup
1. From the project root, init a new node project:
   ```
   npm init
   ```

2. Install testing library:
   - macOS/Linux: `npm install --save-dev jest`


3. Check npm script for testing:
   - Edit package.json
   - Add inside `scripts` property, `"test": "jest"
   `
### Ready to go
- Run `npm run test` and enjoy a smooth test-driven flow.
