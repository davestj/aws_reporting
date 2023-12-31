import argparse
import datetime
import boto3
import pandas as pd


class EC2InstanceReport:
    def __init__(self, profile):
        session = boto3.Session(profile_name=profile)
        self.ec2_client = session.client('ec2')
        self.instances = []

    def get_running_instances(self):
        response = self.ec2_client.describe_instances(
            Filters=[{'Name': 'instance-state-name', 'Values': ['running']}]
        )
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                self.instances.append(instance)

    def generate_report(self):
        report_data = []
        for instance in self.instances:
            instance_name = self.get_instance_name(instance)
            instance_id = instance['InstanceId']
            instance_type = instance['InstanceType']
            key_name = instance.get('KeyName', 'N/A')
            launch_time = instance['LaunchTime'].strftime('%Y-%m-%d %H:%M:%S')
            vpc_id = instance['VpcId']
            uptime = self.calculate_uptime(instance['LaunchTime'])
            report_data.append([instance_name, instance_id, instance_type, key_name, uptime, vpc_id])

        df = pd.DataFrame(report_data, columns=['Instance Name', 'Instance ID', 'Instance Type', 'Key Name', 'Uptime', 'VPC ID'])
        filename = f"ec2_instance_report_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.xlsx"
        df.to_excel(filename, index=False)
        print(f"Report generated and saved as '{filename}'.")

    def get_instance_name(self, instance):
        for tag in instance['Tags']:
            if tag['Key'] == 'Name':
                return tag['Value']
        return 'N/A'

    def calculate_uptime(self, launch_time):
        now = datetime.datetime.now(launch_time.tzinfo)
        uptime = now - launch_time
        return str(uptime)

    def run(self):
        self.get_running_instances()
        self.generate_report()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='EC2 Instance Report Generator')
    parser.add_argument('--profile', required=True, help='AWS profile to use for authentication')
    args = parser.parse_args()

    report_generator = EC2InstanceReport(args.profile)
    report_generator.run()

