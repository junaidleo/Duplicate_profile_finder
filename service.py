from fuzzywuzzy import fuzz

from model import Profile

matchingFields = []
ignoredFields = []
nonMatchingFields = []

def find_duplicates(profiles = [], fields = [], profileObject = Profile()):
    if len(profiles) < 2:
        print("No profiles or 1 profile were passed as arguments")
        return
    if len(fields) < 1:
        print("No fields are passed to compare")
    
    if len(profiles) == 2:
        print(duplicate_data(profiles, fields, profileObject))
    else:
        for i in range(len(profiles)-1):
            for j in range(i+1, len(profiles)):
                global matchingFields, ignoredFields, nonMatchingFields
                matchingFields = []
                ignoredFields = []
                nonMatchingFields = []
                print(duplicate_data([profiles[i], profiles[j]], fields, profileObject))


def duplicate_data(profiles = [], fields = [], profileObject = Profile()):
    total_score = 0
    group_fields = [[]]
    all_keys =list(profileObject.get_profile(profiles[-1]).keys())
    ignoredFields.extend(subtract_lists(all_keys, fields))
    ignoredFields.remove('id')
    combination_fields = ['first_name', 'last_name', 'email']

    for field in fields:
        if field in combination_fields:
            group_fields[0].append(field)
        else:
            group_fields.append(field)    
    group_fields[0].sort(key = lambda i: combination_fields.index(i))

    for field in group_fields:
        total_score = get_duplicates_by_field(profiles, field, total_score, profileObject)
        total_score = total_score if total_score > 0 else 0
    matchingFields = subtract_lists(all_keys, ignoredFields)
    matchingFields = subtract_lists(matchingFields, nonMatchingFields)
    matchingFields.remove('id')

    return [profiles, {'total match score': total_score, 'matching_attributes': matchingFields, 'non_matching_attributes': nonMatchingFields, 'ignored_attributes': ignoredFields}]

def get_duplicates_by_field(profiles, field, tot_score, profileObject):
    profile_1 = profileObject.get_profile(profiles[-2])
    profile_2 = profileObject.get_profile(profiles[-1])

    if type(field) is list:
        values = [[], []]
        for i in field:
            if i in profile_1.keys():
                values[0].append(profile_1[i])
            if i in profile_2.keys():
                values[1].append(profile_2[i])
        if fuzz.ratio(" ".join(values[0]), " ".join(values[1])) > 80:
            tot_score += 1
        else:
            nonMatchingFields.extend(field)
    elif field in profile_1.keys() and field in profile_2.keys():
        if profile_1[field] and profile_2[field]:
            if profile_1[field] == profile_2[field]:
                tot_score += 1
            else:
                nonMatchingFields.append(field)
                tot_score -= 1
        else:
            ignoredFields.append(field)

    return tot_score

def subtract_lists(list1, list2):
    return [x for x in list1 if x not in list2]
