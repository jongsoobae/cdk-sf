import aws_cdk as cdk
from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
    aws_s3 as s3,
)
from constructs import Construct


class CdkSfStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        bucket = s3.Bucket(
            self, "heum-staging-a",
            bucket_name="heum-staging-a", removal_policy=cdk.RemovalPolicy.DESTROY)

        # example resource
        # queue = sqs.Queue(
        #     self, "CdkSfQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
