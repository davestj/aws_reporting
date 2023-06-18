# AWS Reporter Series
## Route 53 Zone Report Generator
Script Details: Python 3 class that uses the `boto3` framework to check all active Route 53 hosted zones in Amazon and generate an Excel spreadsheet report with the requested information:

To use this script, make sure you have the `boto3` and `pandas` libraries installed. You can install them using `pip`:

```
pip install boto3 pandas
```

Save the script in a Python file, for example, `route53_zone_report.py`.

To generate the report, run the following command:

```
python route53_zone_report.py --profile your_aws_profile
```

Replace `your_aws_profile` with the AWS profile you want to use for authentication, which should be configured in your AWS credentials file.

The script will retrieve all active Route 53 hosted zones, collect information such as zone name, description, and record count, and generate an Excel spreadsheet report with the collected data. The report will be saved as `route53_zone_report.xlsx` in the same directory as the script.

To access the generated report, follow these steps:

1. Locate the `route53_zone_report.xlsx` file in the same directory as the script.
2. Open the file using any spreadsheet software compatible with Excel files, such as Microsoft Excel, Google Sheets, or LibreOffice Calc.
3. Review the report, which includes the zone name, zone description, and record count for each active hosted zone.

Note: The script assumes you have the necessary permissions to access and list hosted zones using the specified AWS profile.