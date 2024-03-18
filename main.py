import openai
openai.api_key = "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"

def gen_para(topic):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Write a paragraph about the following topic: " + topic,
        max_tokens=700,
        temperature=0.5
    )
    retrieve_blog = response.choices[0].text.strip()
    return retrieve_blog

keep_writing = True
while keep_writing:
    answer = input("Do you want me to write a paragraph? Yes/No ")
    if answer.lower() == "yes":
        topic = input("What do you want me to write a paragraph about? ")
        print(gen_para(topic))
    else:
        keep_writing = False