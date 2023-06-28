from datetime import date
today = date.today()
d1 = today.strftime("%d/%m/%Y")
nodes = [
    {
        "title" : "Journey By Boat",
        "Description" : "Best Journey Ever. I enjoyed lot",
        "time" : "12/1/2023"
    },
    {
        "title" : "Journey By Train",
        "Description" : "Best Journey Ever. I enjoyed lot",
        "time" : "12/1/2023"
    },
    {
        "title" : "Journey By Bus",
        "Description" : "Best Journey Ever. I enjoyed lot",
        "time" : "12/1/2023"
    }
]

title = input("Enter your title: ")
Description = input("Enter description: ")
newNode = {
    "title" : title,
    "Description" : Description,
    "time" : d1
}
nodes.append(newNode)

for node in nodes:
    print(node)

