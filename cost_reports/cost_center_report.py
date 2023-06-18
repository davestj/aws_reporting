import argparse
import boto3
import pandas as pd


class CostCenterReport:
    def __init__(self, profile):
        session = boto3.Session(profile_name=profile)
        self.cost_explorer_client = session.client('ce')

    def get_latest_report(self):
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
        data = []
        for entry in report_data:
            linked_account = entry['Keys'][0]
            cost_center = entry['Keys'][1]
            cost = entry['Metrics']['UnblendedCost']['Amount']
            data.append([linked_account, cost_center, cost])

        df = pd.DataFrame(data, columns=['Linked Account', 'Cost Center', 'Cost'])
        filename = 'cost_center_report.xlsx'
        df.to_excel(filename, index=False)
        print(f"Report generated and saved as '{filename}'.")

    def run(self):
        report_data = self.get_latest_report()
        self.generate_report(report_data)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Cost Center Report Generator')
    parser.add_argument('--profile', required=True, help='AWS profile to use for authentication')
    args = parser.parse_args()

    report_generator = CostCenterReport(args.profile)
    report_generator.run()
