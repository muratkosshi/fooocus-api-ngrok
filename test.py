import replicate

output = replicate.run(
    "google-deepmind/gemma-7b-it:2790a695e5dcae15506138cc4718d1106d0d475e6dca4b1d43f42414647993d5",
    input={
        "top_k": 50,
        "top_p": 0.95,
        "prompt": "Write me a poem about Machine Learning.",
        "temperature": 0.7,
        "max_new_tokens": 512,
        "min_new_tokens": -1,
        "repetition_penalty": 1
    }
)

# The google-deepmind/gemma-7b-it model can stream output as it's running.
# The predict method returns an iterator, and you can iterate over that output.
for item in output:
    # https://replicate.com/google-deepmind/gemma-7b-it/api#output-schema
    print(item, end="")