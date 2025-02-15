# import os
#
# import dotenv
# from openai import OpenAI
#
# dotenv.load_dotenv(os.path.join(os.path.dirname(__file__), "..", "..", ".env", ".env-chatgpt"))
# client = OpenAI()
# completion = client.chat.completions.create(
#     model="gpt-4o-mini",
#     messages=[
#         {"role": "system", "content": "You are a helpful assistant."},
#        Jesteś trenerem programowania w python. Potrafisz przygotowywać flashards na podstawie przesłanych danych. Flashcard powinień być generowany wg schematu w formacie json na podstawie pliku markdown który ci prześlę:
#        {
#         difficulty_level: DifficultyEnum,
#            tags: list[NonEmptyString],
#     ]
# )
#
# print(completion.choices[0].message)
