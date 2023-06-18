import argparse
import boto3
import pandas as pd


class Route53CostEstimate:
    def __init__(self, profile):
        session = boto3.Session(profile_name=profile)
        self.route53_client = session.client('route53')
        self.hosted_zones = []

    def get_active_zones(self):
        response = self.route53_client.list_hosted_zones_by_name()
        self.hosted_zones = response['HostedZones']

    def generate_cost_estimate_report(self):
        report_data = []
        for zone in self.hosted_zones:
            zone_name = zone['Name']
            cost_estimate = self.get_zone_cost_estimate(zone_name)
            report_data.append([zone_name, cost_estimate])

        df = pd.DataFrame(report_data, columns=['Zone Name', 'Cost Estimate'])
        filename = 'route53_cost_estimate_report.xlsx'
        df.to_excel(filename, index=False)
        print(f"Cost estimate report generated and saved as '{filename}'.")

    def get_zone_cost_estimate(self, zone_name):
        response = self.route53_client.get_hosted_zone_cost(Id=zone_name)
        return response['CostEstimate']

    def run(self):
        self.get_active_zones()
        self.generate_cost_estimate_report()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Route 53 Cost Estimate Report Generator')
    parser.add_argument('--profile', required=True, help='AWS profile to use for authentication')
    args = parser.parse_args()

    report_generator = Route53CostEstimate(args.profile)
    report_generator.run()
