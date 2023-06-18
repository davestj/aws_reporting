import argparse
import datetime
import boto3
import pandas as pd


class CostCenterReport:
    def __init__(self, profile):
        session = boto3.Session(profile_name=profile)
        self.cost_explorer_client = session.client('ce')

    def get_latest_report(self):
        """
        Retrieves the latest cost center report from the AWS Cost Explorer API.

        Returns:
        - result: List of dictionaries representing the cost center report data.
        """
        response = self.cost_explorer_client.get_cost_and_usage(
            TimePeriod={
                'Start': '2023-01-01',
                'End': '2023-06-17'
            },
            Granularity='MONTHLY',
            Metrics=[
                'UnblendedCost',
            ],
            GroupBy=[
                {
                    'Type': 'DIMENSION',
                    'Key': 'LINKED_ACCOUNT'
                },
                {
                    'Type': 'DIMENSION',
                    'Key': 'SERVICE'
                }
            ]
        )
        result = response['ResultsByTime'][0]['Groups']
        return result

    def generate_report(self, report_data):
        """
        Generates a cost center report in the form of an Excel spreadsheet.

        Args:
        - report_data: List of dictionaries representing the cost center report data.
        """
        data = []
        for entry in report_data:
            linked_account = entry['Keys'][0]
            cost_center = entry['Keys'][1]
            cost = entry['Metrics']['UnblendedCost']['Amount']
            data.append([linked_account, cost_center, cost])

        df = pd.DataFrame(data, columns=['Linked Account', 'Cost Center', 'Cost'])
        timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        filename = f'cost_center_report_{timestamp}.xlsx'
        df.to_excel(filename, index=False)
        print(f"Report generated and saved as '{filename}'.")

    def run(self):
        """
        Runs the cost center report generation process.
        """
        report_data = self.get_latest_report()
        self.generate_report(report_data)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Cost Center Report Generator')
    parser.add_argument('--profile', required=True, help='AWS profile to use for authentication')
    args = parser.parse_args()

    report_generator = CostCenterReport(args.profile)
    report_generator.run()
