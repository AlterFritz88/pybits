import re
def capitalize_sentences(text: str) -> str:
    """Return text capitalizing the sentences. Note that sentences can end
       in dot (.), question mark (?) and exclamation mark (!)"""
    filtered = list(filter(None, re.split("([\!?.])+", text)))
    ans = ''.join([x.strip()[0].upper() + x.strip()[1:]  if x not in '.!?' else x + " " for x in filtered ]).strip()
    return ans

text = "sdsdsda as a sasas ass saaa. sadsad. sadsd Asdsdsd! dfdf ddSSS? sdddd swef."
print(capitalize_sentences(text))