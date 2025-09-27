def calculate_love_score (name1, name2):
    combined_names = name1 + name2
    lower_case_names = combined_names.lower()
    t = lower_case_names.count('t')
    r = lower_case_names.count('r')
    u = lower_case_names.count('u')
    e = lower_case_names.count('e')
    true = t + r + u + e
    l = lower_case_names.count('l')
    o = lower_case_names.count('o')
    v = lower_case_names.count('v')
    e = lower_case_names.count('e')
    love = l + o + v + e
    love_score = int(str(true) + str(love))
    print(love_score)

