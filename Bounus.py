def capitalSeparater(sentence:str)->str:
    output=""
    if isinstance(sentence, str):
        for i in sentence:
            if  i.isupper():
                i=f" {i.lower()}"
            output+=i
    return output
                    

print(capitalSeparater("helloWorldThere"))