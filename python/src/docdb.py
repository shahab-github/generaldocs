import boto3
from botocore.exceptions import ClientError

class DocumentDBManager:
    def __init__(self, region_name, profile_name=None):
        session = boto3.Session(profile_name=profile_name) if profile_name else boto3.Session()
        self.client = session.client('docdb', region_name=region_name)

    def start(self, cluster_id):
        """
        Start a DocumentDB cluster.
        """
        try:
            response = self.client.start_db_cluster(DBClusterIdentifier=cluster_id)
            return {"status": "started", "response": response}
        except ClientError as e:
            return {"error": str(e)}

    def stop(self, cluster_id):
        """
        Stop a DocumentDB cluster.
        """
        try:
            response = self.client.stop_db_cluster(DBClusterIdentifier=cluster_id)
            return {"status": "stopped", "response": response}
        except ClientError as e:
            return {"error": str(e)}

    def status(self, cluster_id):
        """
        Get the status of a DocumentDB cluster.
        """
        try:
            response = self.client.describe_db_clusters(DBClusterIdentifier=cluster_id)
            status = response['DBClusters'][0]['Status']
            return {"status": status, "response": response}
        except ClientError as e:
            return {"error": str(e)}
