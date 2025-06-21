import pg8000
import os

def lambda_handler(event, context):
    # Database connection settings (use environment variables for security)
    db_host = os.environ['RDS_HOST'].split(':')[0]
    db_user = os.environ['RDS_USER']
    db_password = os.environ['RDS_PASS']
    db_name = os.environ['RDS_DB']
    db_port = 5432  # Default PostgreSQL port
    
    print("Connecting to...")
    print(db_host)
    print(db_user)
    print(db_name)

    try:
        # Create a connection using pg8000
        connection = pg8000.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_name,
            port=db_port
        )
        
        # Test the connection with a simple query
        cursor = connection.cursor()
        cursor.execute("SELECT 1")
        result = cursor.fetchone()
        cursor.close()
        connection.close()
        
        return {
            'statusCode': 200,
            'body': f'Connected successfully to PostgreSQL! Result: {result}'
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': f'Connection failed: {str(e)}'
        }
