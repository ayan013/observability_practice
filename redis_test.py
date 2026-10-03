from dotenv import load_dotenv
import redis, os, time, json

load_dotenv()

r = redis.Redis(
    host='marine-station-point-29909.db.redis.io',
    port=18463,
    decode_responses=True,
    username="default",
    password=os.getenv("REDIS_PASS"),
)


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
    key = f"assessment:{assessment_id}"
    assessment = database[assessment_id]
    if assessment:
        database[assessment_id]["duration"] = new_duration
        r.delete(key)
        return database[assessment_id]
    else:
        return "No data found"

def get_assessment(assessment_id):
    key = f"assessment:{assessment_id}"
    redis_available = True
    try:
        cached_value = r.get(key)
        if cached_value:
            print("Cache HIT")
            value = json.loads(cached_value)
            return value
        print("Cache MISS")
    except redis.exceptions.RedisError:
        redis_available = False
        print("Redis is unavailable")

    assessment = database.get(assessment_id)

    if assessment is None:
        return "Data not found"

    if redis_available:
        try:
            r.set(key,json.dumps(assessment),ex=10)
        except redis.exceptions.RedisError:
            print("Could not connect")

    return assessment


print(get_assessment(101))


print(get_assessment(101))

print(get_assessment(102))