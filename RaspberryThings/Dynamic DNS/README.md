Dinamyc DNS service hosted in raspberry pi and AWS

I hosted a OpenVPN server in one of my raspberry pi, so I can take advantage of Pihole, and connect to any device at home when I'm on the road or whatever.
To do so, I rely on DDNS services offered by 3rd party web sites, but the lack of reliability, spam mails, and the end of the free services era, make me think of this project.

1   Raspberry configuration
Install and configure AWS CLI. See https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html for better guidance.
Set up a new profile
    aws configure
    Enter the required info:
        Access Key
        Secret Key 
        Region 
        JSON
Alter the bash script according to your needs, and grant execution permissions ( chmod +x )
Schedule the execution via Cron

2 AWS configuration

Create a Lambda function with the code provided.
In IAM create a role and add the permissions.

