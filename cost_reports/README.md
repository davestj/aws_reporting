# Cost Center Report Generator

This Python 3 script allows you to generate a cost center report from the AWS Cost Explorer API. The report provides information about the cost incurred for different linked accounts and services associated with your AWS profile. The report is generated in the form of an Excel spreadsheet.

## Prerequisites

- Python 3 installed on your system
- AWS CLI configured with the necessary credentials and permissions
- Required Python packages: `argparse`, `boto3`, `pandas`

## Usage

1. Clone or download the script to your local machine.

2. Install the required Python packages by running the following command:

   ```
   pip install argparse boto3 pandas
   ```

3. Open a terminal or command prompt and navigate to the directory where the script is located.

4. Run the script using the following command:

   ```
   python cost_center_report.py --profile <AWS_PROFILE_NAME>
   ```

   Replace `<AWS_PROFILE_NAME>` with the name of your AWS profile configured in the AWS CLI. This profile should have the necessary permissions to access the AWS Cost Explorer service.

5. The script will fetch the latest cost center report from the AWS Cost Explorer API based on the specified time period (currently set from January 1, 2023, to June 17, 2023) and generate a report in the form

 of an Excel spreadsheet.

6. Once the report is generated, you will see a message indicating the successful generation and the filename of the report, including a timestamp.

   ```
   Report generated and saved as 'cost_center_report_<timestamp>.xlsx'.
   ```

7. Open the generated Excel spreadsheet to view the cost center report.

## Important Note

Make sure you have a stable internet connection and valid AWS credentials with appropriate permissions before running the script.

For further information and support, please refer to the [AWS CLI Documentation](https://docs.aws.amazon.com/cli/index.html) and the official documentation of the AWS Cost Explorer service.

