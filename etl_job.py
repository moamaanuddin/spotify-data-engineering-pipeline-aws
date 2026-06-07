import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsgluedq.transforms import EvaluateDataQuality

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Default ruleset used by all target nodes with data quality enabled
DEFAULT_DATA_QUALITY_RULESET = """
    Rules = [
        ColumnCount > 0
    ]
"""

# Script generated for node albums
albums_node1779370289643 = glueContext.create_dynamic_frame.from_options(format_options={"quoteChar": "\"", "withHeader": True, "separator": ",", "optimizePerformance": False}, connection_type="s3", format="csv", connection_options={"paths": ["s3://glue-quicksight-athena/Staging/albums.csv"], "recurse": True}, transformation_ctx="albums_node1779370289643")

# Script generated for node Amazon S3
AmazonS3_node1779371553398 = glueContext.create_dynamic_frame.from_options(format_options={"quoteChar": "\"", "withHeader": True, "separator": ",", "optimizePerformance": False}, connection_type="s3", format="csv", connection_options={"paths": ["s3://glue-quicksight-athena/Staging/track.csv"], "recurse": True}, transformation_ctx="AmazonS3_node1779371553398")

# Script generated for node artists
artists_node1779370287637 = glueContext.create_dynamic_frame.from_options(format_options={"quoteChar": "\"", "withHeader": True, "separator": ",", "optimizePerformance": False}, connection_type="s3", format="csv", connection_options={"paths": ["s3://glue-quicksight-athena/Staging/artists.csv"], "recurse": True}, transformation_ctx="artists_node1779370287637")

# Script generated for node Join
Join_node1779370338209 = Join.apply(frame1=albums_node1779370289643, frame2=artists_node1779370287637, keys1=["artist_id"], keys2=["id"], transformation_ctx="Join_node1779370338209")

# Script generated for node Join
Join_node1779370816519 = Join.apply(frame1=AmazonS3_node1779371553398, frame2=Join_node1779370338209, keys1=["track_id"], keys2=["track_id"], transformation_ctx="Join_node1779370816519")

# Script generated for node Drop Fields
DropFields_node1779371170578 = DropFields.apply(frame=Join_node1779370816519, paths=["`.track_id`", "id"], transformation_ctx="DropFields_node1779371170578")

# Script generated for node Amazon S3
EvaluateDataQuality().process_rows(frame=DropFields_node1779371170578, ruleset=DEFAULT_DATA_QUALITY_RULESET, publishing_options={"dataQualityEvaluationContext": "EvaluateDataQuality_node1779370283819", "enableDataQualityResultsPublishing": True}, additional_options={"dataQualityResultsPublishing.strategy": "BEST_EFFORT", "observations.scope": "ALL"})
AmazonS3_node1779371190455 = glueContext.write_dynamic_frame.from_options(frame=DropFields_node1779371170578, connection_type="s3", format="glueparquet", connection_options={"path": "s3://glue-quicksight-athena/DataWarehouse/", "partitionKeys": []}, format_options={"compression": "snappy"}, transformation_ctx="AmazonS3_node1779371190455")

job.commit()
