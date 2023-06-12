# pinglog
Logging to personal discord server

# Install
1. Clone the repository
2. cd pinglog 
3. pip install . 


# Example Usage 

    from pinglog import pinglog 
    logger = pinglog.Logger() 
    logger.set_webhook('<webhook to server>') 
    logger.ping('hello world') 
