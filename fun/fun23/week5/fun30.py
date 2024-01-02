
# matching input with a specific case
def http_error(status):
    match status:
        case 400:
            return 'Bad request'
        case 404:
            return 'not found'
        case 418:
            return 'I am a teapot'
        case _:
            return 'something is wrong with the internet'
        
# main execution
if __name__ == '__main__':
    print(http_error(400))