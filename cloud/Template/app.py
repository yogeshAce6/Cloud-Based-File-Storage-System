import boto3
import os
from flask import Flask, request, render_template_string

app = Flask(_name_)

S3_BUCKET_NAME = 'cloudbasedfilestorage'  # your bucket name
s3 = boto3.client('s3', region_name='us-east-1')

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file part'
        file = request.files['file']
        if file.filename == '':
            return 'No selected file'
        try:
            s3.upload_fileobj(file, S3_BUCKET_NAME, file.filename)
            return 'File uploaded successfully!'
        except Exception as e:
            return f'Error uploading file: {e}'
            
             return render_template_string(html_form)

if _name_ == '_main_':
    app.run(debug=True, host='0.0.0.0')