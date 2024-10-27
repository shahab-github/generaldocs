import boto3
from botocore.exceptions import ClientError

def get_documentdb_clusters():
    # Define the regions to search in
    regions = ['us-east-1', 'us-west-2']
    clusters_info = []

    for region in regions:
        try:
            # Create a DocumentDB client for each region
            client = boto3.client('docdb', region_name=region)

            # Get the list of DB clusters
            response = client.describe_db_clusters()

            # Extract relevant information
            for cluster in response.get('DBClusters', []):
                cluster_info = {
                    'cluster_id': cluster['DBClusterIdentifier'],
                    'status': cluster['Status'],
                    'region': region
                }
                clusters_info.append(cluster_info)
        
        except ClientError as e:
            print(f"Error retrieving clusters in region {region}: {e}")
        except Exception as e:
            print(f"An unexpected error occurred in region {region}: {e}")
    
    return clusters_info

def get_cluster_status(cluster_name):
    # Get the list of clusters across specified regions
    clusters = get_documentdb_clusters()

    # Find and return the status of the specified cluster
    for cluster in clusters:
        if cluster['cluster_id'] == cluster_name:
            return cluster['status']
    
    print(f"Cluster '{cluster_name}' not found in any region.")
    return None  # Return None if the cluster is not found

# Example usage
if __name__ == "__main__":
    cluster_name = 'your-cluster-name'  # Replace with your cluster name
    status = get_cluster_status(cluster_name)
    
    if status:
        print(f"The status of the cluster '{cluster_name}' is: {status}")
    else:
        print(f"Cluster '{cluster_name}' not found.")
