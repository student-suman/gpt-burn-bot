# from openai import OpenAI;
# # const openai = new OpenAI();

# client = OpenAI(
#     api_key ="" --> use your own apikeys
# )
# completion = client.chat.completions.create(
#     model="gpt-4o-mini",
#     messages= [
#         { "role": "system", "content": "You are a helpful assistant." },
#         {
#             "role": "user",
#             "content": "Write a haiku about recursion in programming.",
#         },
#     ],
# )
# print(completion.choices[0].message)



# import openai

# # Initialize OpenAI client with API key
# openai.api_key = "your-api-key"  # Replace with your actual API key

# # Send a request to OpenAI API
# response = openai.ChatCompletion.create(
#     model="gpt-4o-mini",
#     messages=[
#         {"role": "system", "content": "You are a helpful assistant."},
#         {"role": "user", "content": "Write a haiku about recursion in programming."},
#     ],
# )

# # Print the response
# print(response["choices"][0]["message"]["content"])

