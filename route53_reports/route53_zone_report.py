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
            #record_count = self.get_record_count(zone['Id'])
            report_data.append([zone_name, zone_description])

        df = pd.DataFrame(report_data, columns=['Zone Name', 'Zone Description'])
        filename = 'route53_zone_report.xlsx'
        df.to_excel(filename, index=False)
        print(f"Report generated and saved as '{filename}'.")


    def run(self):
        self.get_active_zones()
        self.generate_report()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Route 53 Zone Report Generator')
    parser.add_argument('--profile', required=True, help='AWS profile to use for authentication')
    args = parser.parse_args()

    report_generator = Route53ZoneReport(args.profile)
    report_generator.run()
