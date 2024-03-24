import sqlalchemy
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql:/db_user:ybbRxOnxGyreiasnQ2Yzpg@4bbas-db-cluster-9142.7tc.aws-eu-central-1.cockroachlabs.cloud:26257/postssite?sslmode=verify-full")

print(sqlalchemy.__version__)