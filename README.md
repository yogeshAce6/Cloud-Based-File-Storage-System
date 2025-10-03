# Cloud-Based-File-Storage-System

## Project Description

This project implements a cloud-based file storage system using AWS S3 for scalable storage solutions. It provides a user-friendly interface for file uploads and downloads, with secure access control.

## Technologies

- **AWS S3**: For scalable file storage
- **Python**: Programming language used
- **Flask**: Web framework for Python
- **HTML/CSS**: For the user interface

## Key Features

- **File Uploads**: Allows users to upload files to AWS S3.
- **File Downloads**: Generates secure URLs for file access.
- **User Interface**: Simple HTML form for file uploads.

## Setup Instructions

### Create S3 Bucket
1. BucketName Should Be Unique.
2. Block All The public Access.
3. Click The CheckBox.
4. Click CreateBucket.
![imageAlt](https://github.com/yogeshAce6/Cloud-Based-File-Storage-System/blob/03103f9236b49febbdfbe56728c3f1b0c3e05016/cloud/Homepage%20_%20S3%20_%20us-east-1%20and%2010%20more%20pages%20-%20Personal%20-%20Microsoft%E2%80%8B%20Edge%2003-10-2025%2014_11_10.png)

### 1. Launch an EC2 Instance

1. Log in to AWS Management Console and launch an EC2 instance with Ubuntu Server.
2. Configure the security group to allow HTTP (port 80), HTTPS (port 443), and SSH (port 22),CoustomTcp(port 5000).
3.Launch Instance.

![imageAlt](https://github.com/yogeshAce6/Cloud-Based-File-Storage-System/blob/d57f196708764ff0212b5d35318cb77f57ae3d9c/cloud/Launch%20an%20instance%20_%20EC2%20_%20us-east-1%20-%20Google%20Chrome%2003-10-2025%2014_34_02.png)

4.After Launch Instances.

![imageAlt](https://github.com/yogeshAce6/Cloud-Based-File-Storage-System/blob/29c56b071eb36a519a512e86c7c35df44411fd8c/cloud/codecloudbasedfilestorage%20-%20S3%20bucket%20_%20S3%20_%20us-east-1%20and%206%20more%20pages%20-%20Personal%20-%20Microsoft%E2%80%8B%20Edge%2001-10-2025%2018_54_49.png)

### 2. Connect to Your EC2 Instance

```bash
ssh -i "your-key-pair.pem" ubuntu@your-ec2-public-dns

sudo yum update -y 
sudo yum install python3-pip -y 
pip3 --version 
pip3 install Flask boto3 
mkdir file_storage_app 
cd file_storage_app 
nano app.py 
this will open nano text editor where we have to paste a code
 import boto3
import os
from flask import Flask, request, render_template_string

app = Flask(_name_)

S3_BUCKET_NAME = 'endsemproj'  # your bucket name
s3 = boto3.client('s3', region_name='ap-south-1')

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
    
    # Styled HTML form
    html_form = '''
    <!doctype html>
    <html>
    <head>
        <title>Upload File</title>
        <style>
            body {
                margin: 0;
                padding: 0;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(to right, #74ebd5, #ACB6E5);
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }

            .upload-box {
                background-color: white;
                padding: 40px;
                border-radius: 12px;
                box-shadow: 0 8px 16px rgba(0,0,0,0.2);
                text-align: center;
                width: 350px;
            }

            h1 {
                color: #333;
                margin-bottom: 20px;
            }

            input[type="file"] {
                margin: 20px 0;
                padding: 10px;
                border: 1px solid #ccc;
                border-radius: 6px;
                width: 100%;
            }

            input[type="submit"] {
                background-color: #4CAF50;
                color: white;
                padding: 12px 24px;
                border: none;
                border-radius: 6px;
                cursor: pointer;
                font-size: 16px;
                width: 100%;
            }

            input[type="submit"]:hover {
                background-color: #45a049;
            }
        </style>
    </head>
    <body>
        <div class="upload-box">
            <h1>Upload a New File</h1>
            <form method="post" enctype="multipart/form-data">
                <input type="file" name="file"><br>
                <input type="submit" value="Upload">
            </form>
        </div>
    </body>
    </html>
    '''
    return render_template_string(html_form)

if _name_ == '_main_':
    app.run(debug=True, host='0.0.0.0')
ctrl+o , enter , ctrl+x 
 
python3 app.py 
http://13.233.120.153:5000/   // Your public ipv4 of ec2and port 5000 to open website
```

### final Output will

![imageAlt](https://github.com/yogeshAce6/Cloud-Based-File-Storage-System/blob/53d4471d15bb3891d62d90fd63a93952ee1f580a/cloud/codecloudbasedfilestorage%20-%20S3%20bucket%20_%20S3%20_%20us-east-1%20and%206%20more%20pages%20-%20Personal%20-%20Microsoft%E2%80%8B%20Edge%2001-10-2025%2018_55_19.png)

![imageAlt](https://github.com/yogeshAce6/Cloud-Based-File-Storage-System/blob/df88d557407f9ad770e189b8a5757f8aeb278c33/cloud/Upload%20File%20and%206%20more%20pages%20-%20Personal%20-%20Microsoft%E2%80%8B%20Edge%2001-10-2025%2018_51_33.png)
