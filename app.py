
locodb_obj = {
    "path" : "./file.locodb"
}

def nextSerial():

    file = open(locodb_obj["path"], "r")
    data = file.readlines()
    file.close()
    data_f = []

    for x in data:
        data_f.append(x.strip())
    numbers = []
    
    for x in data_f:
        numbers.append(int(x.split(",")[0].split(":")[-1]))
    
    if len(numbers)!=0:
        return max(numbers)+1
    else:
        return 1


def create_data(dict):

    content = "pkey:" + str(nextSerial()) + ","
    for k in list(dict.keys()):
        content = content + str(k) + ":" + str(dict[k]) + ","
    file = open(locodb_obj["path"], "r")
    data = file.readlines()
    file.close()
    dataLines = []

    for x in data:
        dataLines.append(x.strip())
    dataLines.append(content)
    newContent = ""

    for x in dataLines:
        newContent += x + "\n"
    wFile = open(locodb_obj["path"], "w")
    wFile.write(newContent)
    wFile.close()
    print("Data inserted successfully")


def read_data(pk=None):

    file = open(locodb_obj["path"], "r")
    obj_with_pk = {}
    obj_without_pk = []
    data = file.readlines()
    file.close()
    stripped_data = []
    for line in data:
        stripped_data.append(line.strip())
    if pk is not None:
        for i in stripped_data:
            if i.split(",")[0].split(":")[-1] == str(pk):
                for x in i.split(","):
                    obj_with_pk[x.split(":")[0]] = x.split(":")[-1]
                break
        return obj_with_pk
          
    else :
        obj_without_pk = []
        dyn_dict = {}
        ind = 0
        for i in stripped_data :
            for j in i.split(","):
                dyn_dict[j.split(":")[0]] = j.split(":")[-1]
            obj_without_pk.append(dyn_dict)
            dyn_dict = {}
        return obj_without_pk
    

def delete_data(pk):

    file = open(locodb_obj["path"], "r")
    data = file.readlines()
    file.close()

    data_f = []

    if isinstance(pk, int):
        for x in data:
            data_f.append(x.strip())
        for y in data_f:
            if str(y.split(",")[0].split(":")[-1]) == str(pk):
                data_f.remove(y)
        content = ""
        for z in data_f:
            content = content + z + "\n"
        file1 = open(locodb_obj["path"], "w")
        file1.write(content)
        file1.close()
        print("Data deleted successfully")

    elif isinstance(pk, list):
        for x in data:
            data_f.append(x.strip())
        for y in data_f:
            if int(y.split(",")[0].split(":")[-1]) in pk:
                data_f.remove(y)
        content = ""
        for z in data_f:
            content = content + z + "\n"
        file1 = open(locodb_obj["path"], "w")
        file1.write(content)
        file1.close()
        print("Data deleted successfully")

def isItemPresent(target, destination):
    for y in destination:
        if target.split(":")[0] == y.split(":")[0]:
            destination.remove(y)
            destination.append(f"")

def update_data(pk,target):
    file = open(locodb_obj["path"], "r")
    data = file.readlines()
    file.close()
    data_f = []
    for x in data:
        data_f.append(x.strip())
    for y in data_f:
        for dt in y.split(","):
            if dt.split(":")[0] == target.split(":")[0]:
                y.split(",").remove(dt)
                t = y.split(",").append(f"{target[list(target.keys())[0]]}:{target[list(target.keys())[-1]]}")
                dt.remove(y)
                dt.append(t)
                

update_data("1", {"city" : "Agartala"})