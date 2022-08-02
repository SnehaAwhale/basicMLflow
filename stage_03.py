import mlflow
with open('test.txt','a+') as f:
    last_text=f.write('added lines')

    mlflow.log_metrics(last_text)
    print('End of stage_03')