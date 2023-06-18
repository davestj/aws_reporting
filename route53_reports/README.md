AWS Reporter Series
Script Details: Python 3 class that uses the `boto3` framework to check all active Route 53 hosted zones in Amazon and generate an Excel spreadsheet report with the requested information:

```python
import argparse
import boto3
import pandas as pd


class Route53ZoneReport:
    def __init__(self, profile):
        session = boto3.Session(profile_name=profile)
        self.route53_client = session.client('route53')
        self.hosted_zones = []

    def get_active_zones(self):
        response = self.route53_client.list_hosted_zones_by_name()
        self.hosted_zones = response['HostedZones']

    def generate_report(self):
        report_data = []
        for zone in self.hosted_zones:
            zone_name = zone['Name']
            zone_description = zone.get('Config', {}).get('Comment', 'N/A')
            record_count = self.get_record_count(zone['Id'])
            report_data.append([zone_name, zone_description, record_count])

        df = pd.DataFrame(report_data, columns=['Zone Name', 'Zone Description', 'Record Count'])
        filename = 'route53_zone_report.xlsx'
        df.to_excel(filename, index=False)
        print(f"Report generated and saved as '{filename}'.")

    def get_record_count(self, zone_id):
        response = self.route53_client.get_hosted_zone_count(Id=zone_id)
        return response['Count']

    def run(self):
        self.get_active_zones()
        self.generate_report()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Route 53 Zone Report Generator')
    parser.add_argument('--profile', required=True, help='AWS profile to use for authentication')
    args = parser.parse_args()

    report_generator = Route53ZoneReport(args.profile)
    report_generator.run()
```

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