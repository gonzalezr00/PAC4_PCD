# PAC 4 - PCD - Cyclist Analysis Project

This project performs data analysis on cyclists, using a dataset provided in `data/dataset.csv`. The analysis is carried out through a series of modules that transform and analyze the data.

## Project Structure

- `ex1_module.py`: Loads and prepares the initial DataFrame.
- `ex2_module.py`: Performs a transformation on the DataFrame.
- `ex3_module.py`: Performs another transformation on the DataFrame.
- `ex4_module.py`: Performs an additional transformation on the DataFrame.
- `ex5_module.py`: Performs specific analysis on UCSC cyclists.

## Requirements

To run this project, you need to have Python and the dependencies listed in `requirements.txt` installed.

## Installation

1. Clone this repository:
    ```sh
    git clone https://github.com/gonzalezr00/PAC4_PCD.git # use --branch master to load the back up
    cd PAC4_PCD
    ```

2. Create a virtual environment and install the dependencies:
    For linux:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```
    
    For Windows:
    ```sh
    python -m venv venv
    Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass # In case you encounter an excecution error
    `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

    On macOS, use:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    pip3 install -r requirements.txt
    ```


## Execution

To run the analysis, simply execute the file:
```sh
python main.py
```

On macOS, use:
```sh
python3 main.py
```


## Testing

The tests for this project are located in `test.py`. To execute the tests, run the following command:

```sh
python -m unittest test.py
```

On macOS, use:
```sh
python3 -m unittest test.py
```
