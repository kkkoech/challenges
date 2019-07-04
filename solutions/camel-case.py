def to_camel_case(text):
    if text.strip() == "":
        return ""
    indices_dash = [i for i, x in enumerate(text) if x == "-"]
    indices_underscore = [i for i, x in enumerate(text) if x == "_"]
    indices = indices_underscore + indices_dash
    text_list = list(text)
    '''
    def capitalize_str(pos):
        text_list[pos] = text_list[pos].capitalize()
        return text_list
    '''
    for pos in indices:
        text_list[pos+1] = text_list[pos+1].capitalize()
    #map(lambda x: capitalize_str(x+1),indices)
    text_list = filter(lambda x: x!= "-",text_list)
    text_list = filter(lambda x: x!= "_",text_list)
    return "".join(text_list)

print(to_camel_case("wesleyan_u-sucks"))
