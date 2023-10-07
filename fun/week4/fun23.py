
# copy of collection
def collection_copy(dict):
    for user, status in dict.copy().items():
        if status == 'inactive':
            del dict[user]

def new_collection(dict):
    new_dict = {}
    for user, status in dict.items():
        if status == 'active':
            new_dict[user] = status
    return new_dict

# main execution
if __name__ == '__main__':
    # copy collection
    work_status = {'Fredrik' : 'active', 'Ola' : 'inactive', 'Elinor' : 'active'}
    print(work_status)
    collection_copy(work_status)
    print(work_status)

    # new collection
    work_status = {'Fredrik' : 'active', 'Ola' : 'inactive', 'Elinor' : 'active'}
    print(work_status)
    work_status = new_collection(work_status)
    print(work_status)