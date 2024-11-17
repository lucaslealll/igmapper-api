# Setting Up the Development Environment

## Prerequisites

- **Python 3.10** must be installed on your system.

## Steps for Setting Up

1. **Create a local virtual environment:**
  ```sh
  python3.10 -m venv .venv
  ```

2. **Activate the virtual environment:**
   
    Close the terminal and reopen it. This will help ensure that the virtual environment is activated correctly. If you are using `VS Code`, it may ask if you want to change the runtime to the one you just created.

*If the environment is not activated automatically, use the following command*:

- Linux, macOS:
  ```sh
  source .venv/bin/activate
  ```
- Windows:
  ```cmd
  .venv\Scripts\activate
  ```

1. **Install the required libraries:**
  ```sh
  pip install -r requirements.txt
  ```

1. **The directory is ready to use.**

---

### Additional Notes

- To deactivate the virtual environment, you can use the command:
  ```sh
  deactivate
  ```
  - Every time you open the project in VS Code, it will be identified and initialized automatically.
- Make sure that all dependencies are listed in the `requirements.txt` file to ensure that the environment is configured correctly.