from flask import Flask
import boto3


app = Flask(__name__)

@app.route('/')
def hello():
    create_service()
    return "Running the Flask App to create container"




def create_service():
    client = boto3.client("ecs", region_name="us-west-2")
    response = client.create_service(cluster='CustomerCluster', 
                serviceName="SimpleWebServer-Customer1",
                taskDefinition='xxxxxx',
                desiredCount=1,
                loadBalancers=[
                    {
                        'targetGroupArn': 'arn:aws:elasticloadbalancing:us-west-2:xxxxxxx:targetgroup/Customer/xxxxxxx',
                        'containerName': 'xxxxx',
                        'containerPort': 80
                    },
                ],
                networkConfiguration={
                    'awsvpcConfiguration': {
                        'subnets': [
                            'subnet-xxxxx','subnet-xxxxx'
                        ],
                        'assignPublicIp': 'ENABLED',
                        'securityGroups': ["sg-xxxxxx"]
                    }
                },
                launchType='FARGATE',
            )    

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
