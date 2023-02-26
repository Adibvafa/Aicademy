import openai

openai.api_key = "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"
#openai.Model.list()
#print("\n\nLinked Lists in Computer Science\n\nLinked lists are a fundamental data structure used in computer science. They are a type of linear data structure, meaning they store data in a linear fashion. Unlike arrays, linked lists are dynamic in size and can grow or shrink as needed.\n\nA linked list consists of nodes, which are the individual elements of the list. Each node contains a data element and a pointer to the next node in the list. This makes it possible to traverse the list in a linear fashion.\n\nPictures\n\n[Insert Pictures]\n\nLinked lists are useful in a variety of applications, such as sorting and searching data. They can also be used to implement stacks and queues, which are also important data structures in computer science.\n\nLinked lists are also used in graph algorithms, such as depth-first search and breadth-first search. These algorithms traverse the graph by following the edges of the graph, which are represented by the linked list.\n\nPictures\n\n[Insert Pictures]\n\nLinked lists are an important data structure in computer science, used in a variety of applications. This course has discussed how linked lists are structured, how they are used in sorting and searching data, and how they are used in graph algorithms.\n\nThis course has provided an overview of linked lists in computer science, including their structure, uses, and applications. It has also discussed how linked lists are used in graph algorithms, such as depth-first search and breadth-first search. The course has also included pictures to illustrate the concepts discussed.")
#list1 = [1, 2, 3, 4]
#list2 = [5, 6, 7, 8]

#list3 = list1 + list2

#print(list3)
subject = input("Please enter what you would like to take a short course on. The more specific you are, the more specific the course will be:")
response = openai.Completion.create(
  model="text-davinci-003",
  prompt=f"Generate an introduction that has the subject \"{subject}\" which could accomidate pictures in between",
  temperature=0.5,
  max_tokens=3700,
  frequency_penalty=0.0,
  presence_penalty=0.0
)
intro = response["choices"][0]["text"]
response = openai.Completion.create(
  model="text-davinci-003",
  prompt=f"Generate 5 multiple choice problems and solutions on the subject \"{subject}\" which could accomidate pictures in between. for example, a python course could have which of these would print hello world 100 times: a) print('hello world') b) sadfgsfg c)sdrfsdfg d)for i in range(100): print('hello world') and the answer would be d.",
  temperature=0.5,
  max_tokens=3700,
  frequency_penalty=0.0,
  presence_penalty=0.0
)
problems = response["choices"][0]["text"]
response = openai.Completion.create(
  model="text-davinci-003",
  prompt=f"Generate a summary on the subject \"{subject}\" which could accomidate pictures in between",
  temperature=0.5,
  max_tokens=3700,
  frequency_penalty=0.0,
  presence_penalty=0.0
)
summary = response["choices"][0]["text"]
print(intro, problems, summary)
