import mlflow
textadd='/n text added from stage02'

with open('test.txt','a+') as f:
    f.write(textadd)
    readfile=f.read()
    mlflow.log_param(textadd)
    print('end of stage_02')