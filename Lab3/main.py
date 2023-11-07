# Exercitiul 1

def set_operations(a, b):
    intersection = set(a) & set(b)
    union = set(a) | set(b)
    a_difference = set(a) - set(b)
    b_difference = set(b) - set(a)

    result = [intersection, union, a_difference, b_difference]
    return result


list_a = [1, 2, 3, 4, 5]
list_b = [3, 4, 5, 6, 7]

print("\nEXERCITIUL 1:")
sets_result = set_operations(list_a, list_b)
print("Intersection:", sets_result[0])
print("Union:", sets_result[1])
print("A - B:", sets_result[2])
print("B - A:", sets_result[3])


# Exercitiul 2

def count_characters(text):
    character_count = {}
    for char in text:
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1
    return character_count


print("\nEXERCITIUL 2:")
print(count_characters("Ana has apples."))


# Exercitiul 3

def compare_dictionaries(dict1, dict2):
    if not isinstance(dict1, dict) or not isinstance(dict2, dict):
        return False

    if set(dict1.keys()) != set(dict2.keys()):
        return False

    for key in dict1:
        value1 = dict1[key]
        value2 = dict2[key]

        if isinstance(value1, dict) and isinstance(value2, dict):
            if not compare_dictionaries(value1, value2):
                return False
        else:
            if value1 != value2:
                return False

    return True


print("\nEXERCITIUL 3:")
dict1 = {'a': 1, 'b': [2, 3, {'c': 4}], 'd': {'e': 5}}
dict2 = {'a': 1, 'b': [2, 3, {'c': 4}], 'd': {'e': 5}}
print(compare_dictionaries(dict1, dict2))


# Exercitiul 4

def build_xml_element(tag, content, **attributes):
    xml_element = f"<{tag}"

    for key, value in attributes.items():
        xml_element += f' {key}="{value}"'

    xml_element += f">{content}</{tag}>"

    return xml_element


print("\nEXERCITIUL 4:")
xml_element = build_xml_element("a", "Hello there", href="http://python.org", _class="my-link", id="someid")
print(xml_element)


# Exercitiul 5

def validate_dict(rules, dictionary):
    for key, prefix, middle, suffix in rules:
        if key in dictionary:
            value = dictionary[key]
            if (not prefix or value.startswith(prefix)) and \
               (not suffix or value.endswith(suffix)) and \
               (middle in value and not value.startswith(middle) and not value.endswith(middle)):
                continue
            else:
                return False
        else:
            return False
    return True


rules = {("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}
data = {
    "key1": "come inside, it's too cold out",
    "key3": "this is not valid",
    "key2": "start of winter in the middle"
}
print("\nEXERCITIUL 5:")
print(validate_dict(rules, data))


# Exercitiul 6

def count_unique_and_duplicates(input_list):
    unique_set = set()
    duplicate_set = set()

    for item in input_list:
        if item in unique_set:
            duplicate_set.add(item)
        else:
            unique_set.add(item)

    unique_count = len(unique_set)
    duplicate_count = len(duplicate_set)

    return (unique_count, duplicate_count)


my_list = [1, 2, 2, 3, 4, 4, 5]
print("\nEXERCITIUL 6:")
print(count_unique_and_duplicates(my_list))


# Exercitiul 7

def set_operations(*sets):
    operations = {}

    for i, set1 in enumerate(sets):
        for j, set2 in enumerate(sets):
            if i != j:
                key = f"{set1} | {set2}"
                operations[key] = set1 | set2

                key = f"{set1} & {set2}"
                operations[key] = set1 & set2

                key = f"{set1} - {set2}"
                operations[key] = set1 - set2

                key = f"{set2} - {set1}"
                operations[key] = set2 - set1

    return operations


set1 = {1, 2}
set2 = {2, 3}
set3 = {3, 4}
print("\nEXERCITIUL 7:")
results = set_operations(set1, set2, set3)
for key, value in results.items():
    print(f"{key}: {value}")


# Exercitiul 8

def loop(mapping):
    visited = set()
    current_key = "start"
    objects = []

    while current_key not in visited and current_key in mapping:
        visited.add(current_key)
        objects.append(mapping[current_key])
        next_key = mapping[current_key]

        if next_key == current_key:
            break

        current_key = next_key

    if current_key in objects:
        idx = objects.index(current_key)
        objects = objects[:idx + 1]

    return objects


mapping = {'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}
print("\nEXERCITIUL 8:")
print(loop(mapping))


# Exercitiul 9

def count_matching_args(*args, **kwargs):
    positional_args_set = set(args)
    keyword_values_set = set(kwargs.values())

    matching_args = positional_args_set.intersection(keyword_values_set)
    count = len(matching_args)

    return count


print("\nEXERCITIUL 9:")
result = count_matching_args(1, 2, 3, 4, x=1, y=2, z=3, w=5)
print("returna", result)
