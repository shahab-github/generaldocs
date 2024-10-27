import boto3

def get_documentdb_clusters():
    # Define the regions to search in
    regions = ['us-east-1', 'us-west-2']
    clusters_info = []

    for region in regions:
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
    
    return clusters_info

def get_cluster_status(cluster_name):
    # Get the list of clusters across specified regions
    clusters = get_documentdb_clusters()
    
    # Find and return the status of the specified cluster
    for cluster in clusters:
        if cluster['cluster_id'] == cluster_name:
            return cluster['status']
    
    return None  # Return None if the cluster is not found

# Example usage
if __name__ == "__main__":
    cluster_name = 'your-cluster-name'  # Replace with your cluster name
    status = get_cluster_status(cluster_name)
    
    if status:
        print(f"The status of the cluster '{cluster_name}' is: {status}")
    else:
        print(f"Cluster '{cluster_name}' not found.")
