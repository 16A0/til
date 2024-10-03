from pyspark.sql import SparkSession
import csv
import chardet

# Initialize Spark session
spark = SparkSession.builder.appName("CSVHandler").getOrCreate()

# Sample data: Replace this with your DataFrame containing the CSV column
data = [("1", "name,age,job\nJohn,30,Developer\nJane,25,Designer")]
df = spark.createDataFrame(data, ["id", "csv_column"])

# Function to process CSV column
def process_csv_column(csv_content):
    # Detect encoding
    result = chardet.detect(csv_content.encode())
    encoding = result['encoding']
    
    # Detect delimiter
    sniffer = csv.Sniffer()
    dialect = sniffer.sniff(csv_content)
    delimiter = dialect.delimiter
    
    # Read CSV content into a DataFrame
    csv_rdd = spark.sparkContext.parallelize([csv_content])
    csv_df = spark.read.option("delimiter", delimiter).option("header", True).csv(csv_rdd)
    
    return csv_df, encoding, delimiter

# Apply the function to the DataFrame
processed_dfs = df.rdd.map(lambda row: process_csv_column(row.csv_column)).collect()

# Show the processed DataFrames and other details
for processed_df, encoding, delimiter in processed_dfs:
    print(f"Encoding: {encoding}")
    print(f"Delimiter: {delimiter}")
    processed_df.show()

# Stop the Spark session
spark.stop()
