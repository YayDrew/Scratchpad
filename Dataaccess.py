import psycopg 

def getlines(usefile, questionFile):
    if usefile: 
        # Open the file safely using 'with' so it's closed properly, even if there's an error
        with open(questionFile) as f:
            lines = f.readlines()
    else: 
        connection=connect_to_db()
        # Use a hardcoded fallback list of questions
        lines = [
            'Who invented the backwards worm?~Owen',
            'Who was a powerful landscaper?~Drew'
        ]
    return lines

def connect_to_db():
    try:
        '''Adjust these parameters for your setup
        "host=localhost port=5432 dbname=postgres user=postgres sslmode=prefer connect_timeout=10'''
        conn = psycopg.connect(
            dbname="postgres",
            user="postgres",
            password="admin123",
            host="localhost",
            port=5432
        )
        print("✅ Connection successful")
        return conn
    except Exception as e:
        print("❌ Connection failed:", e)
        return None
