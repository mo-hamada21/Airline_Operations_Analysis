# Airline Operations Analysis

## Overview
This project focuses on analyzing airline operations using a dataset containing monthly statistics for various airlines across different countries. The analysis includes key metrics such as passenger and freight traffic, categorized by incoming and outgoing flows.

---

## Dataset Description
The dataset used in this project provides detailed information about airline operations, including:

- **Month**: Month of the year (e.g., Jan-85).
- **Airline**: Name of the airline (e.g., Air China).
- **Port_Country**: Country associated with the airport/port.
- **Passengers_In**: Number of incoming passengers.
- **Freight_In_(tonnes)**: Volume of incoming freight in tonnes.
- **Mail_In_(tonnes)**: Volume of incoming mail in tonnes.
- **Passengers_Out**: Number of outgoing passengers.
- **Freight_Out_(tonnes)**: Volume of outgoing freight in tonnes.
- **Mail_Out_(tonnes)**: Volume of outgoing mail in tonnes.
- **Year**: Year of the recorded data.
- **Month_num**: Numeric representation of the month (e.g., 1 for January).

---

## Tools and Libraries
The following libraries and tools are utilized in the project:

- **Pandas**: For data manipulation and analysis.
- **NumPy**: For numerical computations.
- **Matplotlib**: For creating static, animated, and interactive visualizations.
- **Seaborn**: For statistical data visualization.

---

## Key Features
- **Data Loading**: Efficiently loads and previews airline data.
- **Exploratory Data Analysis (EDA)**: Provides insights into passenger and freight trends across airlines and countries.
- **Visualization**: Utilizes Matplotlib and Seaborn for clear and informative visualizations.
- **Custom Functions**: Leverages custom utilities for streamlined analysis.

---

## Usage
### Requirements
Ensure you have the following installed:
- Python 3.7+
- Required Python libraries listed in `requirements.txt`

### Steps to Run the Project
1. Clone this repository:
   ```bash
   git clone https://github.com/your-repo/airline-analysis.git
   ```
2. Navigate to the project directory:
   ```bash
   cd airline-analysis
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Open the Jupyter Notebook:
   ```bash
   jupyter notebook Project.ipynb
   ```
5. Run the notebook cells sequentially to execute the analysis.

---

## Output
The analysis generates:
1. Summarized insights into airline operations by country and month.
2. Interactive and static visualizations showing trends in passenger and freight data.

---

## Project Structure
```
├── Project.ipynb       # Jupyter Notebook with the analysis
├── requirements.txt    # Required Python dependencies
├── HelperFunctions.py  # Custom utility functions
├── data
│   └── airline_portcountry.csv  # Input dataset
└── README.md           # Project documentation
```

---

## Contributing
Contributions are welcome! Please fork this repository and submit a pull request for any improvements or new features.

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

## Contact
For any questions or feedback, feel free to reach out at:
- **Email**: your-email@example.com
- **GitHub**: [your-github-handle](https://github.com/your-github-handle)
