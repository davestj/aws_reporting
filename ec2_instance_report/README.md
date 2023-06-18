# AWS Reporter Series
## EC2 Instance Report Generator
Python 3 class that uses the `boto3` framework to check all active running EC2 instances 
in Amazon and generate an Excel spreadsheet report with the requested information:

To use this script, make sure you have the `boto3` and `pandas` libraries installed. You can install them using `pip`:

```
pip install boto3 pandas
```

Save the script in a Python file, for example, `ec2_instance_report.py`.

To generate the report, run the following command:

```
python ec2_instance_report.py --profile your_aws_profile
```

Replace `your_aws_profile` with the AWS profile you want to use for authentication, which should be configured in your AWS credentials file.

The script will retrieve all active running EC2 instances, collect information such as instance name, ID, size, key, uptime, and VPC ID, and generate an Excel spreadsheet report with the collected data. The report will be saved as a file with a timestamp in the filename, e.g., `ec2_instance_report_20220101234567.xlsx`.

You can access the generated report by opening the file using any spreadsheet software compatible with Excel files, such as Microsoft Excel, Google Sheets, or LibreOffice Calc.

Note: The script assumes you have the necessary permissions to access and describe EC2 instances using the specified AWS
