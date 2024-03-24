# postswithflask
Posts Website

export DATABASE_URL="cockroachdb://db_user:ybbRxOnxGyreiasnQ2Yzpg@4bbas-db-cluster-9142.7tc.aws-eu-central-1.cockroachlabs.cloud:26257/postssite?sslmode=verify-full"
db_user
ybbRxOnxGyreiasnQ2Yzpg
export DATABASE_URL="postgresql://db_user:REVEAL_PASSWORD@4bbas-db-cluster-9142.7tc.aws-eu-central-1.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full"

certificate
mkdir -p $env:appdata\postgresql\; Invoke-WebRequest -Uri https://cockroachlabs.cloud/clusters/1d221a66-b750-4718-9542-b8d92f6ac9b6/cert -OutFile $env:appdata\postgresql\root.crt


import os
from sqlalchemy import create_engine, text

engine = create_engine(os.environ["DATABASE_URL"])
conn = engine.connect()

res = conn.execute(text("SELECT now()")).fetchall()
print(res)