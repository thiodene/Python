# Uploading Files on Google Drive using Python
The Drive API allows you to upload file data when creating or updating a File resource.

# You can send upload requests in any of the following ways:

Simple upload: uploadType=media. For quick transfer of a small file (5 MB or less). To perform a simple upload, refer to Performing a Simple Upload.
Multipart upload: uploadType=multipart. For quick transfer of a small file (5 MB or less) and metadata describing the file, all in a single request. To perform a multipart upload, refer to Performing a Multipart Upload.
Resumable upload: uploadType=resumable. For more reliable transfer, especially important with large files. Resumable uploads are a good choice for most applications, since they also work for small files at the cost of one additional HTTP request per upload. To perform a resumable upload, refer to Performing a Resumable Upload.
Most Google API client libraries implement at least one of the methods. Refer to the client library documentation for additional details on how to use each of the methods.

# Source:
https://developers.google.com/drive/api/v3/manage-uploads
https://developers.google.com/api-client-library/python/start/get_started
