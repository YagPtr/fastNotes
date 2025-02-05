import json


# def response_to_dict(data):
#     data = json.bumps(data)
#     dictionary = []
#     for i in data:
#         dictionary.append({i: data[i]})
#     #

#     # # print(dictionary)
#     # for i in dictionary:
#     #     print(i, dictionary[i])
#     # print(dictionary)
#     return dictionary


def result_to_response(data):
    dictionary = []

    for item in data:
        # print(item)
        dictionary.append({"id": item.id, "data": str(item.data), "note": item.name})

    # print(dictionary)

    return json.dumps(dictionary, ensure_ascii=False)
