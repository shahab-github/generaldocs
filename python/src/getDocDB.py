import boto3

def get_documentdb_clusters(region_name):
    # Create a DocumentDB client
    client = boto3.client('docdb', region_name=region_name)

    # Get the list of DB clusters
    response = client.describe_db_clusters()
    
    # Extract relevant information
    clusters_info = []
    for cluster in response.get('DBClusters', []):
        cluster_info = {
            'cluster_id': cluster['DBClusterIdentifier'],
            'status': cluster['Status'],
            'region': region_name
        }
        clusters_info.append(cluster_info)
    
    return clusters_info

def get_cluster_status(cluster_name, region_name):
    # Get the list of clusters
    clusters = get_documentdb_clusters(region_name)
    
    # Find and return the status of the specified cluster
    for cluster in clusters:
        if cluster['cluster_id'] == cluster_name:
            return cluster['status']
    
    return None  # Return None if the cluster is not found

# Example usage
if __name__ == "__main__":
    region = 'us-east-1'  # Specify your region
    cluster_name = 'your-cluster-name'  # Replace with your cluster name
    status = get_cluster_status(cluster_name, region)
    
    if status:
        print(f"The status of the cluster '{cluster_name}' is: {status}")
    else:
        print(f"Cluster '{cluster_name}' not found.")
