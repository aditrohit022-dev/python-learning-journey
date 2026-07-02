import requests 
def fetch_random_user_free_api():
    url="https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response=requests.get(url)
    print(response)  
    data=response.json 
    if data["success"] and "data" in data:
        user_data=data["data"]
        username= user_data["login"]["username"]
        countryname= user_data["location"]["country"]
        return username,countryname
    else:
        raise Exception ("failed to fetch user data!") 
        
        
def main():
    try:
        username,countryname=(f"username:{username}\n country:{countryname}")
        fetch_random_user_free_api()
    except Exception as e:
        print(str(e))  
        
    
    
    
    
    
    
    
    if __name__=='__main__':
        main()
