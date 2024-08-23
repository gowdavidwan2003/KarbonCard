# Financial Data Processing Web App(Done as a part of KarbonCard Hackathon)

This web application is designed to process financial data from a JSON file and evaluate various financial flags. It uses functions defined in `model.py` to compute the flags and displays the results with color-coded indicators.

## Features

- **File Upload**: Upload a JSON file containing financial data.
- **Data Processing**: Computes various financial flags based on the provided data.
- **Results Display**: Shows the computed flags with color-coded indicators representing different risk levels.

## Requirements

- Python 3.7 or higher
- Streamlit
- JSON

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/financial-data-web-app.git
   cd financial-data-web-app
   ```

2. **Install Dependencies**

   Ensure you have Python and pip installed. Install the required packages using:

   ```bash
   pip install streamlit
   ```


### Running the App

1. **Start the Streamlit Server**

   Run the following command in your terminal:

   ```bash
   streamlit run app.py
   ```

2. **Access the App**

   After starting the server, open your web browser and navigate to the local server URL, typically `http://localhost:8501`.

### Usage

1. **Upload a JSON File**

   On the main page, use the file uploader to select and upload a JSON file containing the financial data. The file should adhere to the expected format, with a `"data"` key containing the financial information.

2. **View Results**

   After uploading the file, the app will process the data and display results on the same page. Results include:

   - **Total Revenue Flag**: Indicates if total revenue exceeds 50 million.
   - **Borrowing to Revenue Ratio Flag**: Shows the ratio of borrowings to revenue.
   - **Interest Service Coverage Ratio (ISCR) Flag**: Indicates the company’s ability to cover its interest payments.

   Each flag is color-coded as follows:

   - **GREEN**: Value `1`
   - **AMBER**: Value `2`
   - **RED**: Value `0`
   - **MEDIUM_RISK**: Value `3`
   - **WHITE**: Value `4`


### Troubleshooting

- **JSON Decode Errors**: Ensure the uploaded file is a valid JSON format.
- **Missing Keys**: Verify the JSON structure matches the required format.

For any issues or questions, please contact me at gowdavidwan2003@gmail.com or 7975045560.

