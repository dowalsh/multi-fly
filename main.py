# hello world
def main():
    print("Hello World")
    # read in api key from file
    with open('api_key.txt', 'r') as file:
        api_key = file.read().replace('\n', '')
    
    print(api_key)

if __name__ == '__main__':
    main()