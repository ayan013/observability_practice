cache = {}

database = {
    101: {
        "id": 101,
        "title": "Python Backend Assessment",
        "duration": 60
    },
    102: {
        "id": 102,
        "title": "SQL Assessment",
        "duration": 45
    }
}


def get_assessment(assessment_id):
    for id, assessment in database.items():
        if id == assessment_id:
            if cache.get(id):
                print("Cache HIT")
                return cache[id]
            new_id = id
            new_data = assessment
            cache[new_id] = new_data
            print("Cache MISS")
            return assessment
    return "No data found"

while True:
    assess_id = int(input("Insert ID:- "))
    print(get_assessment(assess_id))