import json


def result_to_response(data):
    dictionary = []

    for item in data:
        # print(item)
        dictionary.append({"id": item.id, "data": str(item.data), "note": item.name})

    return json.dumps(dictionary, ensure_ascii=False)
