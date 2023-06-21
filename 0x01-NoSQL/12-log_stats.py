from pymongo import MongoClient

def nginx_logs_stats():
    # Connect to MongoDB
    client = MongoClient('mongodb://localhost:27017/')
    
    # Access the logs database and nginx collection
    db = client['logs']
    collection = db['nginx']
    
    # Get the total number of documents in the collection
    total_logs = collection.count_documents({})
    print(f"Total logs: {total_logs}")
    
    # Get the number of documents for each HTTP method
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\t{method}: {count}")
    
    # Get the number of documents with method=GET and path=/status
    count_status = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"method=GET path=/status: {count_status}")
    
    # Close the MongoDB connection
    client.close()

# Run the script
nginx_logs_stats()
