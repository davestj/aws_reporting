# AWS Reporter series
# Python3 EC2 Instance Report Generator

This Python 3 script allows you to generate a report of all the active running EC2 instances in your AWS account and save it as an Excel spreadsheet. The report includes information such as the instance name, instance ID, instance type, key name, uptime, and VPC ID.

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
   python ec2_instance_report.py --profile <AWS_PROFILE_NAME>
   ```

   Replace `<AWS_PROFILE_NAME>` with the name of your AWS profile configured in the AWS CLI. This profile should have the necessary permissions to access EC2 instances.

5. The script will fetch the running EC2 instances and generate a report in the form of an Excel spreadsheet. The report file will be named `ec2_instance_report_<timestamp>.xlsx`, where `<timestamp>` represents the current date and time in the format `YYYYMMDDHHMMSS`.

6. Once the report is generated, you will see a message indicating the successful generation and the filename of the report.

   ```
   Report generated and saved as 'ec2_instance_report_<timestamp>.xlsx'.
   ```

7. Open the generated Excel spreadsheet to view the EC2 instance report.


**Note:** This script requires a stable internet connection and proper AWS credentials to access the EC2 service.

# Python3 Route 53 Zone Report Generator

This Python 3 script allows you to generate a report of active Route 53 hosted zones in AWS and save it as an Excel spreadsheet. The report includes the zone name, zone description, and the number of records in each zone.

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
   python route53_zone_report.py --profile <AWS_PROFILE_NAME>
   ```

   Replace `<AWS_PROFILE_NAME>` with the name of your AWS profile configured in the AWS CLI. This profile should have the necessary permissions to access Route 53 hosted zones.

5. The script will fetch the active hosted zones and generate a report in the form of an Excel spreadsheet named `route53_zone_report.xlsx`. The report will be saved in the same directory where the script is located.

   The report will contain three columns: 'Zone Name', 'Zone Description', and 'Record Count'.

6. Once the report is generated, you will see a message indicating the successful generation and the filename of the report.

   ```
   Report generated and saved as 'route53_zone_report.xlsx'.
   ```

7. Open the generated Excel spreadsheet to view the Route 53 zone report.

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

5. The script will fetch the latest cost center report from the AWS Cost Explorer API based on the specified time period (currently set from January 1, 2023, to June 17, 2023) and generate a report in the form of an Excel spreadsheet. The report file will be named `cost_center_report.xlsx` and will include the following columns

: 'Linked Account', 'Cost Center', and 'Cost'.

6. Once the report is generated, you will see a message indicating the successful generation and the filename of the report.

   ```
   Report generated and saved as 'cost_center_report.xlsx'.
   ```

7. Open the generated Excel spreadsheet to view the cost center report.

## Important Note

Make sure you have properly configured the AWS CLI with the desired AWS profile before running the script. The specified profile should have the necessary permissions to access Route 53 hosted zones.

For further information and support, please refer to the [AWS CLI Documentation](https://docs.aws.amazon.com/cli/index.html).

**Note:** This script requires a stable internet connection and proper AWS credentials to access the Route 53 service.