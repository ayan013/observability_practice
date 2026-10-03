import time
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
def update_assessment(assessment_id, new_duration):
        assessment = database[assessment_id]

        if assessment is None:
            return "No Data found"

        database[assessment_id]["duration"] = new_duration

        if assessment_id in cache:
            del cache[assessment_id]
        return database[assessment_id]


def get_assessment(assessment_id,ttl=10):
    current_time = time.time()
    if assessment_id in cache:
         cache_value = cache[assessment_id]
         if current_time > cache_value["expire"]:
            print("Cache EXPIRED")
            del cache[assessment_id]
         else:
            print("Cache HIT")
            return cache_value["data"]

    assessment = database.get(assessment_id)

    if assessment is None:
        return "No data found"

    print("Cache MISS")

    cache[assessment_id] = {"data": assessment.copy(),
                            "expire": current_time + ttl
                            }

    return assessment

# while True:
#     assess_id = int(input("Insert ID:- "))
print(get_assessment(101))   # MISS → caches 60

update_assessment(101, 90)   # DB updated + cache invalidated

print(get_assessment(101))   # MISS → reads fresh 90

print(get_assessment(101))   # HIT → returns cached 90