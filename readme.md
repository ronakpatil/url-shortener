# URLShortner v0.0.1

### What is URL Shortner?
A URL shortner is an application that converts a regular URL (the web address that starts with http:// ) into its condensed format.

The user only has to copy the full URL of a website and paste it into the URL shortening tool to come up with an abbreviated version that is around 10 to 20 characters long.

### Tools used
- Anaconda Distribution v3.x.x
- VS Code v1.38
- Postman v7.x.x
- Bitly URL Shortener API

### Deployment Steps

1. Get the latest code
    ```
    git pull https://github.com/ronakpatil/url-shortener.git
    ```

2. Navigate to url-shortener directory
    ```
    cd url-shortener/
    ```

3. Create conda environment
    ```
    conda create --name <environment_name> python==3.7
    ``` 

4. Add required packages using requirements file
   ```
   pip install -r requirements.txt
   ```

5. Activate the environmt
   ```
   conda activate <environment_name>
   ```    

6. Navigate to app directory and run app.py file
     (You can run the same using button appear on top-right corner on IDE as well)
    ```
    cd app
    python app.py
    ```

    Flask Server should get started on http://127.0.0.1:5000/

7. Open Postman and add this url
   ```
   http://127.0.0.1:5000/shorturl
   ```

8. Pass query params as
   ```
   actualurl: <url you want to shorten>
   ```
9. Check the response. Short URL will appear there.