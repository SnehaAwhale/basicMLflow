import mlflow

with open('test.txt') as f:
    text=f.read()
    mlflow.log_artifact(f.name, artifact_path="feature")
    # print(f.name)
    print(text)