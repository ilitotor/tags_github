#  brainn.co Challenge

Go to the project directory and build Brainnco image:

```docker build . -t brainnco```

Then run:

 ```docker run brainnco```   
 
 To access the app go to:
 
  ```http://0.0.0.0:8000/repository```
  
  To access the API documentation:
  
 ```http://127.0.0.1:8000/docs#/```

To test:
 
1. Run  ```docker ps```
2. Run ```docker exec -it <container-id> bash  ```
3. Run ```python -m pytest```