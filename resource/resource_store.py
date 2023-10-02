from fastapi import  HTTPException
from botocore.exceptions import NoCredentialsError


class ResourceStore:
    def __init__(self, client, bucket_name):
        self.client = client
        self.bucket_name = bucket_name


    async def upload_file(self,file,object_name):
        try:
            self.client.upload_fileobj(file.file, self.bucket_name, object_name)
            message= "File uploaded successfully"
            return message
        except NoCredentialsError:
            raise HTTPException(status_code=500, detail="AWS credentials not available")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))



    async def get_all_files(self):
        try:
            response = self.client.list_objects_v2(Bucket=self.bucket_name)

            # Extract file names from the response
            file_names = [obj['Key'] for obj in response.get('Contents', [])]

            return file_names
        except Exception as e:
            print(f"Error listing files: {str(e)}")
            return []

    async def get_file(self,file_name):
        try:
            response = self.client.generate_presigned_url('get_object',
                                            Params={'Bucket': self.bucket_name,
                                                    'Key': file_name},
                                            ExpiresIn=3600)
            return response
        except NoCredentialsError:
            raise HTTPException(status_code=500, detail="AWS credentials not available")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
