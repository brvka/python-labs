def find_common_participants(group1, group2, delimeter=","):
    first_part = set(group1.split(delimeter))
    second_part = set(group2.split(delimeter))

    common = first_part.intersection(second_part)

    return sorted(common)


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
print(find_common_participants(participants_first_group, participants_second_group, delimeter="|"))
